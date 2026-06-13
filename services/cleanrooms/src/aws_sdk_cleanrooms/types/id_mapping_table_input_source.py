"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdMappingTableInputSource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.id_namespace_type


class IdMappingTableInputSource(TypedDict):
    id_namespace_association_id: "str"
    """<p>The unique identifier of the ID namespace association.</p>"""
    type: "aws_sdk_cleanrooms.types.id_namespace_type.IdNamespaceType"
    """<p>The type of the input source of the ID mapping table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingTableInputSource) -> dict:
    out: dict = {}
    out["idNamespaceAssociationId"] = value["id_namespace_association_id"]
    import aws_sdk_cleanrooms.types.id_namespace_type

    out["type"] = aws_sdk_cleanrooms.types.id_namespace_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> IdMappingTableInputSource:
    out: IdMappingTableInputSource = {}  # type: ignore[typeddict-item]
    if "idNamespaceAssociationId" in data:
        out["id_namespace_association_id"] = data["idNamespaceAssociationId"]
    else:
        raise DeserializationError(
            "IdMappingTableInputSource.id_namespace_association_id required"
        )
    if "type" in data:
        import aws_sdk_cleanrooms.types.id_namespace_type

        out["type"] = aws_sdk_cleanrooms.types.id_namespace_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("IdMappingTableInputSource.type required")
    return out
