"""Generated from Smithy shape ``com.amazonaws.autoscaling#DeleteLifecycleHookType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.ascii_string_max_len255
    import capo_auto_scaling.types.xml_string_max_len255


class DeleteLifecycleHookType(TypedDict, closed=True):
    lifecycle_hook_name: NotRequired[
        "capo_auto_scaling.types.ascii_string_max_len255.AsciiStringMaxLen255"
    ]
    """<p>The name of the lifecycle hook.</p>"""
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteLifecycleHookType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "lifecycle_hook_name" in value:
        pairs.append((f"{prefix}.LifecycleHookName", str(value["lifecycle_hook_name"])))
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )


def deserialize_query(el: Element) -> DeleteLifecycleHookType:
    out: DeleteLifecycleHookType = {}  # type: ignore[typeddict-item]
    child_lifecycle_hook_name = el.find("LifecycleHookName")
    if child_lifecycle_hook_name is not None:
        out["lifecycle_hook_name"] = str(child_lifecycle_hook_name.text or "")
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    return out
