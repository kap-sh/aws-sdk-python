"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateConfiguredTableAssociationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_table_association


class CreateConfiguredTableAssociationOutput(TypedDict, closed=True):
    configured_table_association: (
        "capo_cleanrooms.types.configured_table_association.ConfiguredTableAssociation"
    )
    """<p>The configured table association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredTableAssociationOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.configured_table_association

    out["configuredTableAssociation"] = (
        capo_cleanrooms.types.configured_table_association.serialize_json(
            value["configured_table_association"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateConfiguredTableAssociationOutput:
    out: CreateConfiguredTableAssociationOutput = {}  # type: ignore[typeddict-item]
    if "configuredTableAssociation" in data:
        import capo_cleanrooms.types.configured_table_association

        out["configured_table_association"] = (
            capo_cleanrooms.types.configured_table_association.deserialize_json(
                data["configuredTableAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConfiguredTableAssociationOutput.configured_table_association required"
        )
    return out
