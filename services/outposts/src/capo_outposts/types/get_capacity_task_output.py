"""Generated from Smithy shape ``com.amazonaws.outposts#GetCapacityTaskOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.asset_id
    import capo_outposts.types.capacity_task_failure
    import capo_outposts.types.capacity_task_id
    import capo_outposts.types.capacity_task_status
    import capo_outposts.types.dry_run
    import capo_outposts.types.instances_to_exclude
    import capo_outposts.types.iso8601_timestamp
    import capo_outposts.types.order_id
    import capo_outposts.types.outpost_id
    import capo_outposts.types.requested_instance_pools
    import capo_outposts.types.task_action_on_blocking_instances


class GetCapacityTaskOutput(TypedDict, closed=True):
    capacity_task_id: NotRequired["capo_outposts.types.capacity_task_id.CapacityTaskId"]
    """<p>ID of the capacity task.</p>"""
    outpost_id: NotRequired["capo_outposts.types.outpost_id.OutpostId"]
    """<p>ID of the Outpost associated with the specified capacity task.</p>"""
    order_id: NotRequired["capo_outposts.types.order_id.OrderId"]
    """<p>ID of the Amazon Web Services Outposts order associated with the specified capacity task.</p>"""
    asset_id: NotRequired["capo_outposts.types.asset_id.AssetId"]
    """<p>The ID of the Outpost asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.</p>"""
    requested_instance_pools: NotRequired[
        "capo_outposts.types.requested_instance_pools.RequestedInstancePools"
    ]
    """<p>List of instance pools requested in the capacity task.</p>"""
    instances_to_exclude: NotRequired[
        "capo_outposts.types.instances_to_exclude.InstancesToExclude"
    ]
    """<p>Instances that the user specified they cannot stop in order to free up the capacity needed to run the capacity task.</p>"""
    dry_run: "capo_outposts.types.dry_run.DryRun"
    """<p>Performs a dry run to determine if you are above or below instance capacity.</p>"""
    capacity_task_status: NotRequired[
        "capo_outposts.types.capacity_task_status.CapacityTaskStatus"
    ]
    """<p>Status of the capacity task.</p> <p>A capacity task can have one of the following statuses:</p> <ul> <li> <p> <code>REQUESTED</code> - The capacity task was created and is awaiting the next step by Amazon Web Services Outposts.</p> </li> <li> <p> <code>IN_PROGRESS</code> - The capacity task is running and cannot be cancelled.</p> </li> <li> <p> <code>FAILED</code> - The capacity task could not be completed.</p> </li> <li> <p> <code>COMPLETED</code> - The capacity task has completed successfully.</p> </li> <li> <p> <code>WAITING_FOR_EVACUATION</code> - The capacity task requires capacity to run. You must stop the recommended EC2 running instances to free up capacity for the task to run.</p> </li> <li> <p> <code>CANCELLATION_IN_PROGRESS</code> - The capacity task has been cancelled and is in the process of cleaning up resources.</p> </li> <li> <p> <code>CANCELLED</code> - The capacity task is cancelled.</p> </li> </ul>"""
    failed: NotRequired["capo_outposts.types.capacity_task_failure.CapacityTaskFailure"]
    """<p>Reason why the capacity task failed.</p>"""
    creation_date: NotRequired["capo_outposts.types.iso8601_timestamp.ISO8601Timestamp"]
    """<p>The date the capacity task was created.</p>"""
    completion_date: NotRequired[
        "capo_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>The date the capacity task ran successfully.</p>"""
    last_modified_date: NotRequired[
        "capo_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>The date the capacity task was last modified.</p>"""
    task_action_on_blocking_instances: NotRequired[
        "capo_outposts.types.task_action_on_blocking_instances.TaskActionOnBlockingInstances"
    ]
    """<p>User-specified option in case an instance is blocking the capacity task from running. Shows one of the following options:</p> <ul> <li> <p> <code>WAIT_FOR_EVACUATION</code> - Checks every 10 minutes over 48 hours to determine if instances have stopped and capacity is available to complete the task.</p> </li> <li> <p> <code>FAIL_TASK</code> - The capacity task fails.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCapacityTaskOutput) -> dict:
    out: dict = {}
    if "capacity_task_id" in value:
        out["CapacityTaskId"] = value["capacity_task_id"]
    if "outpost_id" in value:
        out["OutpostId"] = value["outpost_id"]
    if "order_id" in value:
        out["OrderId"] = value["order_id"]
    if "asset_id" in value:
        out["AssetId"] = value["asset_id"]
    if "requested_instance_pools" in value:
        import capo_outposts.types.requested_instance_pools

        out["RequestedInstancePools"] = (
            capo_outposts.types.requested_instance_pools.serialize_json(
                value["requested_instance_pools"]
            )
        )
    if "instances_to_exclude" in value:
        import capo_outposts.types.instances_to_exclude

        out["InstancesToExclude"] = (
            capo_outposts.types.instances_to_exclude.serialize_json(
                value["instances_to_exclude"]
            )
        )
    out["DryRun"] = value.get("dry_run", False)
    if "capacity_task_status" in value:
        import capo_outposts.types.capacity_task_status

        out["CapacityTaskStatus"] = (
            capo_outposts.types.capacity_task_status.serialize_json(
                value["capacity_task_status"]
            )
        )
    if "failed" in value:
        import capo_outposts.types.capacity_task_failure

        out["Failed"] = capo_outposts.types.capacity_task_failure.serialize_json(
            value["failed"]
        )
    if "creation_date" in value:
        import capo_outposts.types.iso8601_timestamp

        out["CreationDate"] = capo_outposts.types.iso8601_timestamp.serialize_json(
            value["creation_date"]
        )
    if "completion_date" in value:
        import capo_outposts.types.iso8601_timestamp

        out["CompletionDate"] = capo_outposts.types.iso8601_timestamp.serialize_json(
            value["completion_date"]
        )
    if "last_modified_date" in value:
        import capo_outposts.types.iso8601_timestamp

        out["LastModifiedDate"] = capo_outposts.types.iso8601_timestamp.serialize_json(
            value["last_modified_date"]
        )
    if "task_action_on_blocking_instances" in value:
        import capo_outposts.types.task_action_on_blocking_instances

        out["TaskActionOnBlockingInstances"] = (
            capo_outposts.types.task_action_on_blocking_instances.serialize_json(
                value["task_action_on_blocking_instances"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCapacityTaskOutput:
    out: GetCapacityTaskOutput = {}  # type: ignore[typeddict-item]
    if "CapacityTaskId" in data:
        out["capacity_task_id"] = data["CapacityTaskId"]
    if "OutpostId" in data:
        out["outpost_id"] = data["OutpostId"]
    if "OrderId" in data:
        out["order_id"] = data["OrderId"]
    if "AssetId" in data:
        out["asset_id"] = data["AssetId"]
    if "RequestedInstancePools" in data:
        import capo_outposts.types.requested_instance_pools

        out["requested_instance_pools"] = (
            capo_outposts.types.requested_instance_pools.deserialize_json(
                data["RequestedInstancePools"]
            )
        )
    if "InstancesToExclude" in data:
        import capo_outposts.types.instances_to_exclude

        out["instances_to_exclude"] = (
            capo_outposts.types.instances_to_exclude.deserialize_json(
                data["InstancesToExclude"]
            )
        )
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    if "CapacityTaskStatus" in data:
        import capo_outposts.types.capacity_task_status

        out["capacity_task_status"] = (
            capo_outposts.types.capacity_task_status.deserialize_json(
                data["CapacityTaskStatus"]
            )
        )
    if "Failed" in data:
        import capo_outposts.types.capacity_task_failure

        out["failed"] = capo_outposts.types.capacity_task_failure.deserialize_json(
            data["Failed"]
        )
    if "CreationDate" in data:
        import capo_outposts.types.iso8601_timestamp

        out["creation_date"] = capo_outposts.types.iso8601_timestamp.deserialize_json(
            data["CreationDate"]
        )
    if "CompletionDate" in data:
        import capo_outposts.types.iso8601_timestamp

        out["completion_date"] = capo_outposts.types.iso8601_timestamp.deserialize_json(
            data["CompletionDate"]
        )
    if "LastModifiedDate" in data:
        import capo_outposts.types.iso8601_timestamp

        out["last_modified_date"] = (
            capo_outposts.types.iso8601_timestamp.deserialize_json(
                data["LastModifiedDate"]
            )
        )
    if "TaskActionOnBlockingInstances" in data:
        import capo_outposts.types.task_action_on_blocking_instances

        out["task_action_on_blocking_instances"] = (
            capo_outposts.types.task_action_on_blocking_instances.deserialize_json(
                data["TaskActionOnBlockingInstances"]
            )
        )
    return out
