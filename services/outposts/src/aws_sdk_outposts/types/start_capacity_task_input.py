"""Generated from Smithy shape ``com.amazonaws.outposts#StartCapacityTaskInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_outposts.types.asset_id_input
    import aws_sdk_outposts.types.dry_run
    import aws_sdk_outposts.types.instances_to_exclude
    import aws_sdk_outposts.types.order_id
    import aws_sdk_outposts.types.outpost_identifier
    import aws_sdk_outposts.types.requested_instance_pools
    import aws_sdk_outposts.types.task_action_on_blocking_instances


class StartCapacityTaskInput(TypedDict):
    outpost_identifier: "aws_sdk_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>The ID or ARN of the Outposts associated with the specified capacity task.</p>"""
    order_id: NotRequired["aws_sdk_outposts.types.order_id.OrderId"]
    """<p>The ID of the Amazon Web Services Outposts order associated with the specified capacity task.</p>"""
    asset_id: NotRequired["aws_sdk_outposts.types.asset_id_input.AssetIdInput"]
    """<p>The ID of the Outpost asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.</p>"""
    instance_pools: (
        "aws_sdk_outposts.types.requested_instance_pools.RequestedInstancePools"
    )
    """<p>The instance pools specified in the capacity task.</p>"""
    instances_to_exclude: NotRequired[
        "aws_sdk_outposts.types.instances_to_exclude.InstancesToExclude"
    ]
    """<p>List of user-specified running instances that must not be stopped in order to free up the capacity needed to run the capacity task.</p>"""
    dry_run: "aws_sdk_outposts.types.dry_run.DryRun"
    """<p>You can request a dry run to determine if the instance type and instance size changes is above or below available instance capacity. Requesting a dry run does not make any changes to your plan.</p>"""
    task_action_on_blocking_instances: NotRequired[
        "aws_sdk_outposts.types.task_action_on_blocking_instances.TaskActionOnBlockingInstances"
    ]
    """<p>Specify one of the following options in case an instance is blocking the capacity task from running.</p> <ul> <li> <p> <code>WAIT_FOR_EVACUATION</code> - Checks every 10 minutes over 48 hours to determine if instances have stopped and capacity is available to complete the task.</p> </li> <li> <p> <code>FAIL_TASK</code> - The capacity task fails.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCapacityTaskInput) -> dict:
    out: dict = {}
    if "order_id" in value:
        out["OrderId"] = value["order_id"]
    if "asset_id" in value:
        out["AssetId"] = value["asset_id"]
    import aws_sdk_outposts.types.requested_instance_pools

    out["InstancePools"] = (
        aws_sdk_outposts.types.requested_instance_pools.serialize_json(
            value["instance_pools"]
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
    if "task_action_on_blocking_instances" in value:
        import aws_sdk_outposts.types.task_action_on_blocking_instances

        out["TaskActionOnBlockingInstances"] = (
            aws_sdk_outposts.types.task_action_on_blocking_instances.serialize_json(
                value["task_action_on_blocking_instances"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartCapacityTaskInput:
    out: StartCapacityTaskInput = {}  # type: ignore[typeddict-item]
    if "OrderId" in data:
        out["order_id"] = data["OrderId"]
    if "AssetId" in data:
        out["asset_id"] = data["AssetId"]
    if "InstancePools" in data:
        import aws_sdk_outposts.types.requested_instance_pools

        out["instance_pools"] = (
            aws_sdk_outposts.types.requested_instance_pools.deserialize_json(
                data["InstancePools"]
            )
        )
    else:
        raise DeserializationError("StartCapacityTaskInput.instance_pools required")
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
    if "TaskActionOnBlockingInstances" in data:
        import aws_sdk_outposts.types.task_action_on_blocking_instances

        out["task_action_on_blocking_instances"] = (
            aws_sdk_outposts.types.task_action_on_blocking_instances.deserialize_json(
                data["TaskActionOnBlockingInstances"]
            )
        )
    return out
