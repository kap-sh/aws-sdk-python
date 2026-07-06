"""Generated from Smithy shape ``com.amazonaws.autoscaling#DeleteScheduledActionType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class DeleteScheduledActionType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    scheduled_action_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the action to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteScheduledActionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "scheduled_action_name" in value:
        pairs.append(
            (f"{prefix}.ScheduledActionName", str(value["scheduled_action_name"]))
        )


def deserialize_query(el: Element) -> DeleteScheduledActionType:
    out: DeleteScheduledActionType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_scheduled_action_name = el.find("ScheduledActionName")
    if child_scheduled_action_name is not None:
        out["scheduled_action_name"] = str(child_scheduled_action_name.text or "")
    return out
