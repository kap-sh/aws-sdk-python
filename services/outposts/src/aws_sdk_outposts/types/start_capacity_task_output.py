"""Generated from Smithy shape ``com.amazonaws.outposts#StartCapacityTaskOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.asset_id
    import aws_sdk_outposts.types.capacity_task_failure
    import aws_sdk_outposts.types.capacity_task_id
    import aws_sdk_outposts.types.capacity_task_status
    import aws_sdk_outposts.types.dry_run
    import aws_sdk_outposts.types.instances_to_exclude
    import aws_sdk_outposts.types.iso8601_timestamp
    import aws_sdk_outposts.types.order_id
    import aws_sdk_outposts.types.outpost_id
    import aws_sdk_outposts.types.requested_instance_pools
    import aws_sdk_outposts.types.task_action_on_blocking_instances


class StartCapacityTaskOutput(TypedDict, closed=True):
    capacity_task_id: NotRequired[
        "aws_sdk_outposts.types.capacity_task_id.CapacityTaskId"
    ]
    """<p>ID of the capacity task that you want to start.</p>"""
    outpost_id: NotRequired["aws_sdk_outposts.types.outpost_id.OutpostId"]
    """<p>ID of the Outpost associated with the capacity task.</p>"""
    order_id: NotRequired["aws_sdk_outposts.types.order_id.OrderId"]
    """<p>ID of the Amazon Web Services Outposts order of the host associated with the capacity task.</p>"""
    asset_id: NotRequired["aws_sdk_outposts.types.asset_id.AssetId"]
    """<p>The ID of the asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.</p>"""
    requested_instance_pools: NotRequired[
        "aws_sdk_outposts.types.requested_instance_pools.RequestedInstancePools"
    ]
    """<p>List of the instance pools requested in the specified capacity task.</p>"""
    instances_to_exclude: NotRequired[
        "aws_sdk_outposts.types.instances_to_exclude.InstancesToExclude"
    ]
    """<p>User-specified instances that must not be stopped in order to free up the capacity needed to run the capacity task.</p>"""
    dry_run: "aws_sdk_outposts.types.dry_run.DryRun"
    """<p>Results of the dry run showing if the specified capacity task is above or below the available instance capacity.</p>"""
    capacity_task_status: NotRequired[
        "aws_sdk_outposts.types.capacity_task_status.CapacityTaskStatus"
    ]
    """<p>Status of the specified capacity task.</p>"""
    failed: NotRequired[
        "aws_sdk_outposts.types.capacity_task_failure.CapacityTaskFailure"
    ]
    """<p>Reason that the specified capacity task failed.</p>"""
    creation_date: NotRequired[
        "aws_sdk_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>Date that the specified capacity task was created.</p>"""
    completion_date: NotRequired[
        "aws_sdk_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>Date that the specified capacity task ran successfully.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>Date that the specified capacity task was last modified.</p>"""
    task_action_on_blocking_instances: NotRequired[
        "aws_sdk_outposts.types.task_action_on_blocking_instances.TaskActionOnBlockingInstances"
    ]
    """<p>User-specified option in case an instance is blocking the capacity task from running.</p> <ul> <li> <p> <code>WAIT_FOR_EVACUATION</code> - Checks every 10 minutes over 48 hours to determine if instances have stopped and capacity is available to complete the task.</p> </li> <li> <p> <code>FAIL_TASK</code> - The capacity task fails.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCapacityTaskOutput) -> dict:
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
        import aws_sdk_outposts.types.requested_instance_pools

        out["RequestedInstancePools"] = (
            aws_sdk_outposts.types.requested_instance_pools.serialize_json(
                value["requested_instance_pools"]
            )
        )
    if "instances_to_exclude" in value:
        import aws_sdk_outposts.types.instances_to_exclude

        out["InstancesToExclude"] = (
            aws_sdk_outposts.types.instances_to_exclude.serialize_json(
                value["instances_to_exclude"]
            )
        )
    out["DryRun"] = value.get("dry_run", False)
    if "capacity_task_status" in value:
        import aws_sdk_outposts.types.capacity_task_status

        out["CapacityTaskStatus"] = (
            aws_sdk_outposts.types.capacity_task_status.serialize_json(
                value["capacity_task_status"]
            )
        )
    if "failed" in value:
        import aws_sdk_outposts.types.capacity_task_failure

        out["Failed"] = aws_sdk_outposts.types.capacity_task_failure.serialize_json(
            value["failed"]
        )
    if "creation_date" in value:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["CreationDate"] = aws_sdk_outposts.types.iso8601_timestamp.serialize_json(
            value["creation_date"]
        )
    if "completion_date" in value:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["CompletionDate"] = aws_sdk_outposts.types.iso8601_timestamp.serialize_json(
            value["completion_date"]
        )
    if "last_modified_date" in value:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["LastModifiedDate"] = (
            aws_sdk_outposts.types.iso8601_timestamp.serialize_json(
                value["last_modified_date"]
            )
        )
    if "task_action_on_blocking_instances" in value:
        import aws_sdk_outposts.types.task_action_on_blocking_instances

        out["TaskActionOnBlockingInstances"] = (
            aws_sdk_outposts.types.task_action_on_blocking_instances.serialize_json(
                value["task_action_on_blocking_instances"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartCapacityTaskOutput:
    out: StartCapacityTaskOutput = {}  # type: ignore[typeddict-item]
    if "CapacityTaskId" in data:
        out["capacity_task_id"] = data["CapacityTaskId"]
    if "OutpostId" in data:
        out["outpost_id"] = data["OutpostId"]
    if "OrderId" in data:
        out["order_id"] = data["OrderId"]
    if "AssetId" in data:
        out["asset_id"] = data["AssetId"]
    if "RequestedInstancePools" in data:
        import aws_sdk_outposts.types.requested_instance_pools

        out["requested_instance_pools"] = (
            aws_sdk_outposts.types.requested_instance_pools.deserialize_json(
                data["RequestedInstancePools"]
            )
        )
    if "InstancesToExclude" in data:
        import aws_sdk_outposts.types.instances_to_exclude

        out["instances_to_exclude"] = (
            aws_sdk_outposts.types.instances_to_exclude.deserialize_json(
                data["InstancesToExclude"]
            )
        )
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    if "CapacityTaskStatus" in data:
        import aws_sdk_outposts.types.capacity_task_status

        out["capacity_task_status"] = (
            aws_sdk_outposts.types.capacity_task_status.deserialize_json(
                data["CapacityTaskStatus"]
            )
        )
    if "Failed" in data:
        import aws_sdk_outposts.types.capacity_task_failure

        out["failed"] = aws_sdk_outposts.types.capacity_task_failure.deserialize_json(
            data["Failed"]
        )
    if "CreationDate" in data:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["creation_date"] = (
            aws_sdk_outposts.types.iso8601_timestamp.deserialize_json(
                data["CreationDate"]
            )
        )
    if "CompletionDate" in data:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["completion_date"] = (
            aws_sdk_outposts.types.iso8601_timestamp.deserialize_json(
                data["CompletionDate"]
            )
        )
    if "LastModifiedDate" in data:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["last_modified_date"] = (
            aws_sdk_outposts.types.iso8601_timestamp.deserialize_json(
                data["LastModifiedDate"]
            )
        )
    if "TaskActionOnBlockingInstances" in data:
        import aws_sdk_outposts.types.task_action_on_blocking_instances

        out["task_action_on_blocking_instances"] = (
            aws_sdk_outposts.types.task_action_on_blocking_instances.deserialize_json(
                data["TaskActionOnBlockingInstances"]
            )
        )
    return out
