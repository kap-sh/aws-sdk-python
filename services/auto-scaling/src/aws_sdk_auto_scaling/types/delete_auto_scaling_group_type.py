"""Generated from Smithy shape ``com.amazonaws.autoscaling#DeleteAutoScalingGroupType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.force_delete
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class DeleteAutoScalingGroupType(TypedDict):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    force_delete: NotRequired["aws_sdk_auto_scaling.types.force_delete.ForceDelete"]
    """<p>Specifies that the group is to be deleted along with all instances associated with the group, without waiting for all instances to be terminated. This action also deletes any outstanding lifecycle actions associated with the group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteAutoScalingGroupType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "force_delete" in value:
        pairs.append(
            (f"{prefix}.ForceDelete", "true" if value["force_delete"] else "false")
        )


def deserialize_query(el: Element) -> DeleteAutoScalingGroupType:
    out: DeleteAutoScalingGroupType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_force_delete = el.find("ForceDelete")
    if child_force_delete is not None:
        out["force_delete"] = (child_force_delete.text or "").lower() == "true"
    return out
