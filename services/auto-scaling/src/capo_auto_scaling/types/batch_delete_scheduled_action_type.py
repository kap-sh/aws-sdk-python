"""Generated from Smithy shape ``com.amazonaws.autoscaling#BatchDeleteScheduledActionType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.scheduled_action_names
    import capo_auto_scaling.types.xml_string_max_len255


class BatchDeleteScheduledActionType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    scheduled_action_names: NotRequired[
        "capo_auto_scaling.types.scheduled_action_names.ScheduledActionNames"
    ]
    """<p>The names of the scheduled actions to delete. The maximum number allowed is 50. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchDeleteScheduledActionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "scheduled_action_names" in value:
        import capo_auto_scaling.types.scheduled_action_names

        capo_auto_scaling.types.scheduled_action_names.serialize_query(
            value["scheduled_action_names"], pairs, f"{key_prefix}ScheduledActionNames"
        )


def deserialize_query(el: Element) -> BatchDeleteScheduledActionType:
    out: BatchDeleteScheduledActionType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_scheduled_action_names = el.find("ScheduledActionNames")
    if child_scheduled_action_names is not None:
        import capo_auto_scaling.types.scheduled_action_names

        out["scheduled_action_names"] = (
            capo_auto_scaling.types.scheduled_action_names.deserialize_query(
                child_scheduled_action_names
            )
        )
    return out
