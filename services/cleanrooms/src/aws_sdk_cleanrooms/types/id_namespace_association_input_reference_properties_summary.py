"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdNamespaceAssociationInputReferencePropertiesSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.id_namespace_type


class IdNamespaceAssociationInputReferencePropertiesSummary(TypedDict):
    id_namespace_type: "aws_sdk_cleanrooms.types.id_namespace_type.IdNamespaceType"
    """<p>The ID namespace type for this ID namespace association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: IdNamespaceAssociationInputReferencePropertiesSummary,
) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.id_namespace_type

    out["idNamespaceType"] = aws_sdk_cleanrooms.types.id_namespace_type.serialize_json(
        value["id_namespace_type"]
    )
    return out


def deserialize_json(
    data: dict,
) -> IdNamespaceAssociationInputReferencePropertiesSummary:
    out: IdNamespaceAssociationInputReferencePropertiesSummary = {}  # type: ignore[typeddict-item]
    if "idNamespaceType" in data:
        import aws_sdk_cleanrooms.types.id_namespace_type

        out["id_namespace_type"] = (
            aws_sdk_cleanrooms.types.id_namespace_type.deserialize_json(
                data["idNamespaceType"]
            )
        )
    else:
        raise DeserializationError(
            "IdNamespaceAssociationInputReferencePropertiesSummary.id_namespace_type required"
        )
    return out
