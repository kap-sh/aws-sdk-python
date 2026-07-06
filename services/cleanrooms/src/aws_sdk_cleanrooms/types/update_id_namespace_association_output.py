"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateIdNamespaceAssociationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.id_namespace_association


class UpdateIdNamespaceAssociationOutput(TypedDict, closed=True):
    id_namespace_association: (
        "aws_sdk_cleanrooms.types.id_namespace_association.IdNamespaceAssociation"
    )
    """<p>The updated ID namespace association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIdNamespaceAssociationOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.id_namespace_association

    out["idNamespaceAssociation"] = (
        aws_sdk_cleanrooms.types.id_namespace_association.serialize_json(
            value["id_namespace_association"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIdNamespaceAssociationOutput:
    out: UpdateIdNamespaceAssociationOutput = {}  # type: ignore[typeddict-item]
    if "idNamespaceAssociation" in data:
        import aws_sdk_cleanrooms.types.id_namespace_association

        out["id_namespace_association"] = (
            aws_sdk_cleanrooms.types.id_namespace_association.deserialize_json(
                data["idNamespaceAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIdNamespaceAssociationOutput.id_namespace_association required"
        )
    return out
