"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeLifecycleHooksType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.lifecycle_hook_names
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class DescribeLifecycleHooksType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    lifecycle_hook_names: NotRequired[
        "aws_sdk_auto_scaling.types.lifecycle_hook_names.LifecycleHookNames"
    ]
    """<p>The names of one or more lifecycle hooks. If you omit this property, all lifecycle hooks are described.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeLifecycleHooksType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "lifecycle_hook_names" in value:
        import aws_sdk_auto_scaling.types.lifecycle_hook_names

        aws_sdk_auto_scaling.types.lifecycle_hook_names.serialize_query(
            value["lifecycle_hook_names"], pairs, f"{prefix}.LifecycleHookNames"
        )


def deserialize_query(el: Element) -> DescribeLifecycleHooksType:
    out: DescribeLifecycleHooksType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_lifecycle_hook_names = el.find("LifecycleHookNames")
    if child_lifecycle_hook_names is not None:
        import aws_sdk_auto_scaling.types.lifecycle_hook_names

        out["lifecycle_hook_names"] = (
            aws_sdk_auto_scaling.types.lifecycle_hook_names.deserialize_query(
                child_lifecycle_hook_names
            )
        )
    return out
