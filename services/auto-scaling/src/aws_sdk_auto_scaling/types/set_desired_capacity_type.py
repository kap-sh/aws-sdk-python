"""Generated from Smithy shape ``com.amazonaws.autoscaling#SetDesiredCapacityType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.auto_scaling_group_desired_capacity
    import aws_sdk_auto_scaling.types.honor_cooldown
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class SetDesiredCapacityType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    desired_capacity: NotRequired[
        "aws_sdk_auto_scaling.types.auto_scaling_group_desired_capacity.AutoScalingGroupDesiredCapacity"
    ]
    """<p>The desired capacity is the initial capacity of the Auto Scaling group after this operation completes and the capacity it attempts to maintain.</p>"""
    honor_cooldown: NotRequired[
        "aws_sdk_auto_scaling.types.honor_cooldown.HonorCooldown"
    ]
    """<p>Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to complete before initiating a scaling activity to set your Auto Scaling group to its new capacity. By default, Amazon EC2 Auto Scaling does not honor the cooldown period during manual scaling activities.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetDesiredCapacityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "desired_capacity" in value:
        pairs.append((f"{prefix}.DesiredCapacity", str(value["desired_capacity"])))
    if "honor_cooldown" in value:
        pairs.append(
            (f"{prefix}.HonorCooldown", "true" if value["honor_cooldown"] else "false")
        )


def deserialize_query(el: Element) -> SetDesiredCapacityType:
    out: SetDesiredCapacityType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_desired_capacity = el.find("DesiredCapacity")
    if child_desired_capacity is not None:
        out["desired_capacity"] = int(child_desired_capacity.text or "")
    child_honor_cooldown = el.find("HonorCooldown")
    if child_honor_cooldown is not None:
        out["honor_cooldown"] = (child_honor_cooldown.text or "").lower() == "true"
    return out
