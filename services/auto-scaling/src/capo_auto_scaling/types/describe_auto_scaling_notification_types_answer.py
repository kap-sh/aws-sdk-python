"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeAutoScalingNotificationTypesAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.auto_scaling_notification_types


class DescribeAutoScalingNotificationTypesAnswer(TypedDict, closed=True):
    auto_scaling_notification_types: NotRequired[
        "capo_auto_scaling.types.auto_scaling_notification_types.AutoScalingNotificationTypes"
    ]
    """<p>The notification types.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAutoScalingNotificationTypesAnswer,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_notification_types" in value:
        import capo_auto_scaling.types.auto_scaling_notification_types

        capo_auto_scaling.types.auto_scaling_notification_types.serialize_query(
            value["auto_scaling_notification_types"],
            pairs,
            f"{key_prefix}AutoScalingNotificationTypes",
        )


def deserialize_query(el: Element) -> DescribeAutoScalingNotificationTypesAnswer:
    out: DescribeAutoScalingNotificationTypesAnswer = {}  # type: ignore[typeddict-item]
    child_auto_scaling_notification_types = el.find("AutoScalingNotificationTypes")
    if child_auto_scaling_notification_types is not None:
        import capo_auto_scaling.types.auto_scaling_notification_types

        out["auto_scaling_notification_types"] = (
            capo_auto_scaling.types.auto_scaling_notification_types.deserialize_query(
                child_auto_scaling_notification_types
            )
        )
    return out
