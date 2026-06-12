"""Generated from Smithy shape ``com.amazonaws.autoscaling#CancelInstanceRefreshType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.boolean_type
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class CancelInstanceRefreshType(TypedDict):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    wait_for_transitioning_instances: NotRequired[
        "aws_sdk_auto_scaling.types.boolean_type.BooleanType"
    ]
    """<p>When cancelling an instance refresh, this indicates whether to wait for in-flight launches and terminations to complete. The default is true.</p> <p>When set to false, Amazon EC2 Auto Scaling cancels the instance refresh without waiting for any pending launches or terminations to complete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CancelInstanceRefreshType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "wait_for_transitioning_instances" in value:
        pairs.append(
            (
                f"{prefix}.WaitForTransitioningInstances",
                "true" if value["wait_for_transitioning_instances"] else "false",
            )
        )


def deserialize_query(el: Element) -> CancelInstanceRefreshType:
    out: CancelInstanceRefreshType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_wait_for_transitioning_instances = el.find("WaitForTransitioningInstances")
    if child_wait_for_transitioning_instances is not None:
        out["wait_for_transitioning_instances"] = (
            child_wait_for_transitioning_instances.text or ""
        ).lower() == "true"
    return out
