"""Generated from Smithy shape ``com.amazonaws.autoscaling#AttachInstancesQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.instance_ids
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class AttachInstancesQuery(TypedDict, closed=True):
    instance_ids: NotRequired["aws_sdk_auto_scaling.types.instance_ids.InstanceIds"]
    """<p>The IDs of the instances. You can specify up to 20 instances.</p>"""
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AttachInstancesQuery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_ids" in value:
        import aws_sdk_auto_scaling.types.instance_ids

        aws_sdk_auto_scaling.types.instance_ids.serialize_query(
            value["instance_ids"], pairs, f"{prefix}.InstanceIds"
        )
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )


def deserialize_query(el: Element) -> AttachInstancesQuery:
    out: AttachInstancesQuery = {}  # type: ignore[typeddict-item]
    child_instance_ids = el.find("InstanceIds")
    if child_instance_ids is not None:
        import aws_sdk_auto_scaling.types.instance_ids

        out["instance_ids"] = aws_sdk_auto_scaling.types.instance_ids.deserialize_query(
            child_instance_ids
        )
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    return out
