"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceRequirementsWithMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.architecture_type_set
    import capo_ec2.types.instance_requirements_request
    import capo_ec2.types.virtualization_type_set


class InstanceRequirementsWithMetadataRequest(TypedDict, closed=True):
    architecture_types: NotRequired[
        "capo_ec2.types.architecture_type_set.ArchitectureTypeSet"
    ]
    """<p>The architecture type.</p>"""
    virtualization_types: NotRequired[
        "capo_ec2.types.virtualization_type_set.VirtualizationTypeSet"
    ]
    """<p>The virtualization type.</p>"""
    instance_requirements: NotRequired[
        "capo_ec2.types.instance_requirements_request.InstanceRequirementsRequest"
    ]
    """<p>The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceRequirementsWithMetadataRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "architecture_types" in value:
        import capo_ec2.types.architecture_type_set

        capo_ec2.types.architecture_type_set.serialize_ec2_query(
            value["architecture_types"], pairs, f"{key_prefix}ArchitectureTypes"
        )
    if "virtualization_types" in value:
        import capo_ec2.types.virtualization_type_set

        capo_ec2.types.virtualization_type_set.serialize_ec2_query(
            value["virtualization_types"], pairs, f"{key_prefix}VirtualizationTypes"
        )
    if "instance_requirements" in value:
        import capo_ec2.types.instance_requirements_request

        capo_ec2.types.instance_requirements_request.serialize_ec2_query(
            value["instance_requirements"], pairs, f"{key_prefix}InstanceRequirements"
        )


def deserialize_ec2_query(el: Element) -> InstanceRequirementsWithMetadataRequest:
    out: InstanceRequirementsWithMetadataRequest = {}  # type: ignore[typeddict-item]
    if el.find("ArchitectureTypes") is not None:
        import capo_ec2.types.architecture_type_set

        out["architecture_types"] = (
            capo_ec2.types.architecture_type_set.deserialize_ec2_query(
                el, "ArchitectureTypes"
            )
        )
    if el.find("VirtualizationTypes") is not None:
        import capo_ec2.types.virtualization_type_set

        out["virtualization_types"] = (
            capo_ec2.types.virtualization_type_set.deserialize_ec2_query(
                el, "VirtualizationTypes"
            )
        )
    child_instance_requirements = el.find("InstanceRequirements")
    if child_instance_requirements is not None:
        import capo_ec2.types.instance_requirements_request

        out["instance_requirements"] = (
            capo_ec2.types.instance_requirements_request.deserialize_ec2_query(
                child_instance_requirements
            )
        )
    return out
