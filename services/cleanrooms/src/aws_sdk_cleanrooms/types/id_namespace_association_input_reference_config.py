"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdNamespaceAssociationInputReferenceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.id_namespace_association_input_reference_arn


class IdNamespaceAssociationInputReferenceConfig(TypedDict, closed=True):
    input_reference_arn: "aws_sdk_cleanrooms.types.id_namespace_association_input_reference_arn.IdNamespaceAssociationInputReferenceArn"
    """<p>The Amazon Resource Name (ARN) of the Entity Resolution resource that is being associated to the collaboration. Valid resource ARNs are from the ID namespaces that you own.</p>"""
    manage_resource_policies: "bool"
    """<p>When <code>TRUE</code>, Clean Rooms manages permissions for the ID namespace association resource.</p> <p>When <code>FALSE</code>, the resource owner manages permissions for the ID namespace association resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceAssociationInputReferenceConfig) -> dict:
    out: dict = {}
    out["inputReferenceArn"] = value["input_reference_arn"]
    out["manageResourcePolicies"] = value["manage_resource_policies"]
    return out


def deserialize_json(data: dict) -> IdNamespaceAssociationInputReferenceConfig:
    out: IdNamespaceAssociationInputReferenceConfig = {}  # type: ignore[typeddict-item]
    if "inputReferenceArn" in data:
        out["input_reference_arn"] = data["inputReferenceArn"]
    else:
        raise DeserializationError(
            "IdNamespaceAssociationInputReferenceConfig.input_reference_arn required"
        )
    if "manageResourcePolicies" in data:
        out["manage_resource_policies"] = data["manageResourcePolicies"]
    else:
        raise DeserializationError(
            "IdNamespaceAssociationInputReferenceConfig.manage_resource_policies required"
        )
    return out
