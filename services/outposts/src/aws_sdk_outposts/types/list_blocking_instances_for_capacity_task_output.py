"""Generated from Smithy shape ``com.amazonaws.outposts#ListBlockingInstancesForCapacityTaskOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.blocking_instances_list
    import aws_sdk_outposts.types.token


class ListBlockingInstancesForCapacityTaskOutput(TypedDict):
    blocking_instances: NotRequired[
        "aws_sdk_outposts.types.blocking_instances_list.BlockingInstancesList"
    ]
    """<p>A list of all running Amazon EC2 instances on the Outpost. Stopping one or more of these instances can free up the capacity needed to run the capacity task.</p>"""
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]


# --- restJson1 ser/de ---
def serialize_json(value: ListBlockingInstancesForCapacityTaskOutput) -> dict:
    out: dict = {}
    if "blocking_instances" in value:
        import aws_sdk_outposts.types.blocking_instances_list

        out["BlockingInstances"] = (
            aws_sdk_outposts.types.blocking_instances_list.serialize_json(
                value["blocking_instances"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBlockingInstancesForCapacityTaskOutput:
    out: ListBlockingInstancesForCapacityTaskOutput = {}  # type: ignore[typeddict-item]
    if "BlockingInstances" in data:
        import aws_sdk_outposts.types.blocking_instances_list

        out["blocking_instances"] = (
            aws_sdk_outposts.types.blocking_instances_list.deserialize_json(
                data["BlockingInstances"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
