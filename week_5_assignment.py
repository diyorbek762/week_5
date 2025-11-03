
def receive_new_shipments(shipments, new_shipments):
    for new_shipment_item in new_shipments:
        shipments.append(new_shipment_item) # return nothing


def dispatch_shipments(shipments, num_to_dispatch): # (["BOX-A1", "BOX-B2"], 5)
    dispatched_items=[]
    if num_to_dispatch>len(shipments):
        for i in range(len(shipments)):
            removed=shipments.pop(0)
            dispatched_items.append(removed)
            
        # dispatch_shipments = shipments[::]
        # shipments = []
        return dispatched_items # return a full copy of shipments
    while num_to_dispatch>0 and len(shipments)>0:
        removed=shipments.pop(0)
        dispatched_items.append(removed)
        num_to_dispatch -=1
    return dispatched_items

def recall_shipment(shipments, shipment_id):
    if shipment_id in shipments:
        shipments.remove(shipment_id)
        return True
    else:
        return False


def manage_shipments(initial_shipments:list, new_shipments_to_receive, shipments_to_dispatch, shipment_to_recall):
    copy_of_shipments=initial_shipments[::]
    # initial_items=initial_shipments.copy()
    # print(id(initial_shipments))
    # print(id(initial_items))
    receive_new_shipments(copy_of_shipments, new_shipments_to_receive) # use local vars, and not save result
    # print(shipment_with_new_added)
    specified_shipment=recall_shipment(shipments=copy_of_shipments, shipment_id=shipment_to_recall)
    # use local vars, send your copy of shipments as first argument
    dispatching_shipments= dispatch_shipments(shipments=copy_of_shipments, num_to_dispatch=shipments_to_dispatch)
    print('Test Case 1 Results: ')
    print(f'final_state: {copy_of_shipments}')
    print(f'dispatched: {dispatching_shipments}\n')
    print(f'Original list unchanged: {initial_shipments}\n')

initial = ["BOX-A1"]
new = ["BOX-B2", "BOX-C3", "BOX-D4"]
dispatch_count = 2
recall_id = "BOX-C3"
manage_shipments(initial, new_shipments_to_receive=new, shipments_to_dispatch=dispatch_count, shipment_to_recall=recall_id)

initial = ["BOX-A1", "BOX-B2", "BOX-C3", "BOX-D4"]
new = ["BOX-E5", "BOX-F6"]
dispatch_count = 2
recall_id = "BOX-D4"

manage_shipments(initial, new_shipments_to_receive=new, shipments_to_dispatch=dispatch_count, shipment_to_recall=recall_id)


# initial_shipments = ["BOX-001", "BOX-002", "BOX-003", "BOX-004"]
# new_shipments_to_receive = ["BOX-005"]
# shipments_to_dispatch = 1
# shipment_to_recall = "BOX-003"
# manage_shipments(initial_shipments, initial_shipments, shipments_to_dispatch, shipment_to_recall)


# manage_shipments(initial_shipments, 'new_shipments_to_receive')
# Test Case 1 Results:
# final_state: ['BOX-C3', 'BOX-E5', 'BOX-F6']
# dispatched: ['BOX-A1', 'BOX-B2']

# Original list unchanged: ['BOX-A1', 'BOX-B2', 'BOX-C3', 'BOX-D4']