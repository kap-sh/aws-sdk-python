"""Generated from Smithy shape ``com.amazonaws.autoscaling#BatchPutScheduledUpdateGroupActionType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.scheduled_update_group_action_requests
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class BatchPutScheduledUpdateGroupActionType(TypedDict):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    scheduled_update_group_actions: NotRequired[
        "aws_sdk_auto_scaling.types.scheduled_update_group_action_requests.ScheduledUpdateGroupActionRequests"
    ]
    """<p>One or more scheduled actions. The maximum number allowed is 50.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchPutScheduledUpdateGroupActionType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "scheduled_update_group_actions" in value:
        import aws_sdk_auto_scaling.types.scheduled_update_group_action_requests

        aws_sdk_auto_scaling.types.scheduled_update_group_action_requests.serialize_query(
            value["scheduled_update_group_actions"],
            pairs,
            f"{prefix}.ScheduledUpdateGroupActions",
        )


def deserialize_query(el: Element) -> BatchPutScheduledUpdateGroupActionType:
    out: BatchPutScheduledUpdateGroupActionType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_scheduled_update_group_actions = el.find("ScheduledUpdateGroupActions")
    if child_scheduled_update_group_actions is not None:
        import aws_sdk_auto_scaling.types.scheduled_update_group_action_requests

        out["scheduled_update_group_actions"] = (
            aws_sdk_auto_scaling.types.scheduled_update_group_action_requests.deserialize_query(
                child_scheduled_update_group_actions
            )
        )
    return out
