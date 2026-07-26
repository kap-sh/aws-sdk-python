"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeLifecycleHookTypesAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.auto_scaling_notification_types


class DescribeLifecycleHookTypesAnswer(TypedDict, closed=True):
    lifecycle_hook_types: NotRequired[
        "capo_auto_scaling.types.auto_scaling_notification_types.AutoScalingNotificationTypes"
    ]
    """<p>The lifecycle hook types.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeLifecycleHookTypesAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "lifecycle_hook_types" in value:
        import capo_auto_scaling.types.auto_scaling_notification_types

        capo_auto_scaling.types.auto_scaling_notification_types.serialize_query(
            value["lifecycle_hook_types"], pairs, f"{prefix}.LifecycleHookTypes"
        )


def deserialize_query(el: Element) -> DescribeLifecycleHookTypesAnswer:
    out: DescribeLifecycleHookTypesAnswer = {}  # type: ignore[typeddict-item]
    child_lifecycle_hook_types = el.find("LifecycleHookTypes")
    if child_lifecycle_hook_types is not None:
        import capo_auto_scaling.types.auto_scaling_notification_types

        out["lifecycle_hook_types"] = (
            capo_auto_scaling.types.auto_scaling_notification_types.deserialize_query(
                child_lifecycle_hook_types
            )
        )
    return out
