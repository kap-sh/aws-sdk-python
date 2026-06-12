"""Generated from Smithy shape ``com.amazonaws.autoscaling#TerminateInstanceInAutoScalingGroupType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.should_decrement_desired_capacity
    import aws_sdk_auto_scaling.types.xml_string_max_len19


class TerminateInstanceInAutoScalingGroupType(TypedDict):
    instance_id: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len19.XmlStringMaxLen19"
    ]
    """<p>The ID of the instance.</p>"""
    should_decrement_desired_capacity: NotRequired[
        "aws_sdk_auto_scaling.types.should_decrement_desired_capacity.ShouldDecrementDesiredCapacity"
    ]
    """<p>Indicates whether terminating the instance also decrements the size of the Auto Scaling group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TerminateInstanceInAutoScalingGroupType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "should_decrement_desired_capacity" in value:
        pairs.append(
            (
                f"{prefix}.ShouldDecrementDesiredCapacity",
                "true" if value["should_decrement_desired_capacity"] else "false",
            )
        )


def deserialize_query(el: Element) -> TerminateInstanceInAutoScalingGroupType:
    out: TerminateInstanceInAutoScalingGroupType = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_should_decrement_desired_capacity = el.find("ShouldDecrementDesiredCapacity")
    if child_should_decrement_desired_capacity is not None:
        out["should_decrement_desired_capacity"] = (
            child_should_decrement_desired_capacity.text or ""
        ).lower() == "true"
    return out
