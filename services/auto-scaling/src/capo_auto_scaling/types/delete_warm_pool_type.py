"""Generated from Smithy shape ``com.amazonaws.autoscaling#DeleteWarmPoolType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.force_delete
    import capo_auto_scaling.types.xml_string_max_len255


class DeleteWarmPoolType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    force_delete: NotRequired["capo_auto_scaling.types.force_delete.ForceDelete"]
    """<p>Specifies that the warm pool is to be deleted along with all of its associated instances, without waiting for all instances to be terminated. This parameter also deletes any outstanding lifecycle actions associated with the warm pool instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteWarmPoolType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "force_delete" in value:
        pairs.append(
            (f"{prefix}.ForceDelete", "true" if value["force_delete"] else "false")
        )


def deserialize_query(el: Element) -> DeleteWarmPoolType:
    out: DeleteWarmPoolType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_force_delete = el.find("ForceDelete")
    if child_force_delete is not None:
        out["force_delete"] = (child_force_delete.text or "").lower() == "true"
    return out
