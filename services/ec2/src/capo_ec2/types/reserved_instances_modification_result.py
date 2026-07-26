"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesModificationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reserved_instances_configuration
    import capo_ec2.types.string


class ReservedInstancesModificationResult(TypedDict, closed=True):
    reserved_instances_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID for the Reserved Instances that were created as part of the modification request. This field is only available when the modification is fulfilled.</p>"""
    target_configuration: NotRequired[
        "capo_ec2.types.reserved_instances_configuration.ReservedInstancesConfiguration"
    ]
    """<p>The target Reserved Instances configurations supplied as part of the modification request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstancesModificationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "reserved_instances_id" in value:
        pairs.append(
            (f"{prefix}.ReservedInstancesId", str(value["reserved_instances_id"]))
        )
    if "target_configuration" in value:
        import capo_ec2.types.reserved_instances_configuration

        capo_ec2.types.reserved_instances_configuration.serialize_ec2_query(
            value["target_configuration"], pairs, f"{prefix}.TargetConfiguration"
        )


def deserialize_ec2_query(el: Element) -> ReservedInstancesModificationResult:
    out: ReservedInstancesModificationResult = {}  # type: ignore[typeddict-item]
    child_reserved_instances_id = el.find("ReservedInstancesId")
    if child_reserved_instances_id is not None:
        out["reserved_instances_id"] = str(child_reserved_instances_id.text or "")
    child_target_configuration = el.find("TargetConfiguration")
    if child_target_configuration is not None:
        import capo_ec2.types.reserved_instances_configuration

        out["target_configuration"] = (
            capo_ec2.types.reserved_instances_configuration.deserialize_ec2_query(
                child_target_configuration
            )
        )
    return out
