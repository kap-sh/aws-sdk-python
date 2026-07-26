"""Generated from Smithy shape ``com.amazonaws.autoscaling#DetachInstancesQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.instance_ids
    import capo_auto_scaling.types.should_decrement_desired_capacity
    import capo_auto_scaling.types.xml_string_max_len255


class DetachInstancesQuery(TypedDict, closed=True):
    instance_ids: NotRequired["capo_auto_scaling.types.instance_ids.InstanceIds"]
    """<p>The IDs of the instances. You can specify up to 20 instances.</p>"""
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    should_decrement_desired_capacity: NotRequired[
        "capo_auto_scaling.types.should_decrement_desired_capacity.ShouldDecrementDesiredCapacity"
    ]
    """<p>Indicates whether the Auto Scaling group decrements the desired capacity value by the number of instances detached.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DetachInstancesQuery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_ids" in value:
        import capo_auto_scaling.types.instance_ids

        capo_auto_scaling.types.instance_ids.serialize_query(
            value["instance_ids"], pairs, f"{prefix}.InstanceIds"
        )
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "should_decrement_desired_capacity" in value:
        pairs.append(
            (
                f"{prefix}.ShouldDecrementDesiredCapacity",
                "true" if value["should_decrement_desired_capacity"] else "false",
            )
        )


def deserialize_query(el: Element) -> DetachInstancesQuery:
    out: DetachInstancesQuery = {}  # type: ignore[typeddict-item]
    child_instance_ids = el.find("InstanceIds")
    if child_instance_ids is not None:
        import capo_auto_scaling.types.instance_ids

        out["instance_ids"] = capo_auto_scaling.types.instance_ids.deserialize_query(
            child_instance_ids
        )
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_should_decrement_desired_capacity = el.find("ShouldDecrementDesiredCapacity")
    if child_should_decrement_desired_capacity is not None:
        out["should_decrement_desired_capacity"] = (
            child_should_decrement_desired_capacity.text or ""
        ).lower() == "true"
    return out
