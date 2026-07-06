"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdNamespaceAssociationInputReferenceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.id_mapping_workflows_supported
    import aws_sdk_cleanrooms.types.id_namespace_type


class IdNamespaceAssociationInputReferenceProperties(TypedDict, closed=True):
    id_namespace_type: "aws_sdk_cleanrooms.types.id_namespace_type.IdNamespaceType"
    """<p>The ID namespace type for this ID namespace association.</p>"""
    id_mapping_workflows_supported: "aws_sdk_cleanrooms.types.id_mapping_workflows_supported.IdMappingWorkflowsSupported"
    """<p>Defines how ID mapping workflows are supported for this ID namespace association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceAssociationInputReferenceProperties) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.id_namespace_type

    out["idNamespaceType"] = aws_sdk_cleanrooms.types.id_namespace_type.serialize_json(
        value["id_namespace_type"]
    )
    import aws_sdk_cleanrooms.types.id_mapping_workflows_supported

    out["idMappingWorkflowsSupported"] = (
        aws_sdk_cleanrooms.types.id_mapping_workflows_supported.serialize_json(
            value["id_mapping_workflows_supported"]
        )
    )
    return out


def deserialize_json(data: dict) -> IdNamespaceAssociationInputReferenceProperties:
    out: IdNamespaceAssociationInputReferenceProperties = {}  # type: ignore[typeddict-item]
    if "idNamespaceType" in data:
        import aws_sdk_cleanrooms.types.id_namespace_type

        out["id_namespace_type"] = (
            aws_sdk_cleanrooms.types.id_namespace_type.deserialize_json(
                data["idNamespaceType"]
            )
        )
    else:
        raise DeserializationError(
            "IdNamespaceAssociationInputReferenceProperties.id_namespace_type required"
        )
    if "idMappingWorkflowsSupported" in data:
        import aws_sdk_cleanrooms.types.id_mapping_workflows_supported

        out["id_mapping_workflows_supported"] = (
            aws_sdk_cleanrooms.types.id_mapping_workflows_supported.deserialize_json(
                data["idMappingWorkflowsSupported"]
            )
        )
    else:
        raise DeserializationError(
            "IdNamespaceAssociationInputReferenceProperties.id_mapping_workflows_supported required"
        )
    return out
