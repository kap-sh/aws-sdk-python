"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetIdNamespaceAssociationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.id_namespace_association


class GetIdNamespaceAssociationOutput(TypedDict, closed=True):
    id_namespace_association: (
        "aws_sdk_cleanrooms.types.id_namespace_association.IdNamespaceAssociation"
    )
    """<p>The ID namespace association that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdNamespaceAssociationOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.id_namespace_association

    out["idNamespaceAssociation"] = (
        aws_sdk_cleanrooms.types.id_namespace_association.serialize_json(
            value["id_namespace_association"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetIdNamespaceAssociationOutput:
    out: GetIdNamespaceAssociationOutput = {}  # type: ignore[typeddict-item]
    if "idNamespaceAssociation" in data:
        import aws_sdk_cleanrooms.types.id_namespace_association

        out["id_namespace_association"] = (
            aws_sdk_cleanrooms.types.id_namespace_association.deserialize_json(
                data["idNamespaceAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "GetIdNamespaceAssociationOutput.id_namespace_association required"
        )
    return out
