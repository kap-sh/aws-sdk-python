"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdNamespaceIdMappingWorkflowMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.id_mapping_type


class IdNamespaceIdMappingWorkflowMetadata(TypedDict):
    id_mapping_type: "aws_sdk_entityresolution.types.id_mapping_type.IdMappingType"
    """<p>The type of ID mapping.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceIdMappingWorkflowMetadata) -> dict:
    out: dict = {}
    import aws_sdk_entityresolution.types.id_mapping_type

    out["idMappingType"] = (
        aws_sdk_entityresolution.types.id_mapping_type.serialize_json(
            value["id_mapping_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> IdNamespaceIdMappingWorkflowMetadata:
    out: IdNamespaceIdMappingWorkflowMetadata = {}  # type: ignore[typeddict-item]
    if "idMappingType" in data:
        import aws_sdk_entityresolution.types.id_mapping_type

        out["id_mapping_type"] = (
            aws_sdk_entityresolution.types.id_mapping_type.deserialize_json(
                data["idMappingType"]
            )
        )
    else:
        raise DeserializationError(
            "IdNamespaceIdMappingWorkflowMetadata.id_mapping_type required"
        )
    return out
