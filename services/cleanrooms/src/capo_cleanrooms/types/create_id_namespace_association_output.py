"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateIdNamespaceAssociationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.id_namespace_association


class CreateIdNamespaceAssociationOutput(TypedDict, closed=True):
    id_namespace_association: (
        "capo_cleanrooms.types.id_namespace_association.IdNamespaceAssociation"
    )
    """<p>The ID namespace association that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIdNamespaceAssociationOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.id_namespace_association

    out["idNamespaceAssociation"] = (
        capo_cleanrooms.types.id_namespace_association.serialize_json(
            value["id_namespace_association"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateIdNamespaceAssociationOutput:
    out: CreateIdNamespaceAssociationOutput = {}  # type: ignore[typeddict-item]
    if "idNamespaceAssociation" in data:
        import capo_cleanrooms.types.id_namespace_association

        out["id_namespace_association"] = (
            capo_cleanrooms.types.id_namespace_association.deserialize_json(
                data["idNamespaceAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIdNamespaceAssociationOutput.id_namespace_association required"
        )
    return out
