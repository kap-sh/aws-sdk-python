"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceRequirementsWithMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.architecture_type_set
    import aws_sdk_ec2.types.instance_requirements_request
    import aws_sdk_ec2.types.virtualization_type_set


class InstanceRequirementsWithMetadataRequest(TypedDict):
    architecture_types: NotRequired[
        "aws_sdk_ec2.types.architecture_type_set.ArchitectureTypeSet"
    ]
    """<p>The architecture type.</p>"""
    virtualization_types: NotRequired[
        "aws_sdk_ec2.types.virtualization_type_set.VirtualizationTypeSet"
    ]
    """<p>The virtualization type.</p>"""
    instance_requirements: NotRequired[
        "aws_sdk_ec2.types.instance_requirements_request.InstanceRequirementsRequest"
    ]
    """<p>The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceRequirementsWithMetadataRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "architecture_types" in value:
        import aws_sdk_ec2.types.architecture_type_set

        aws_sdk_ec2.types.architecture_type_set.serialize_ec2_query(
            value["architecture_types"], pairs, f"{prefix}.ArchitectureTypes"
        )
    if "virtualization_types" in value:
        import aws_sdk_ec2.types.virtualization_type_set

        aws_sdk_ec2.types.virtualization_type_set.serialize_ec2_query(
            value["virtualization_types"], pairs, f"{prefix}.VirtualizationTypes"
        )
    if "instance_requirements" in value:
        import aws_sdk_ec2.types.instance_requirements_request

        aws_sdk_ec2.types.instance_requirements_request.serialize_ec2_query(
            value["instance_requirements"], pairs, f"{prefix}.InstanceRequirements"
        )


def deserialize_ec2_query(el: Element) -> InstanceRequirementsWithMetadataRequest:
    out: InstanceRequirementsWithMetadataRequest = {}  # type: ignore[typeddict-item]
    if el.find("ArchitectureTypes") is not None:
        import aws_sdk_ec2.types.architecture_type_set

        out["architecture_types"] = (
            aws_sdk_ec2.types.architecture_type_set.deserialize_ec2_query(
                el, "ArchitectureTypes"
            )
        )
    if el.find("VirtualizationTypes") is not None:
        import aws_sdk_ec2.types.virtualization_type_set

        out["virtualization_types"] = (
            aws_sdk_ec2.types.virtualization_type_set.deserialize_ec2_query(
                el, "VirtualizationTypes"
            )
        )
    child_instance_requirements = el.find("InstanceRequirements")
    if child_instance_requirements is not None:
        import aws_sdk_ec2.types.instance_requirements_request

        out["instance_requirements"] = (
            aws_sdk_ec2.types.instance_requirements_request.deserialize_ec2_query(
                child_instance_requirements
            )
        )
    return out
