"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetConfiguredTableAssociationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_table_association


class GetConfiguredTableAssociationOutput(TypedDict, closed=True):
    configured_table_association: (
        "capo_cleanrooms.types.configured_table_association.ConfiguredTableAssociation"
    )
    """<p>The entire configured table association object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfiguredTableAssociationOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.configured_table_association

    out["configuredTableAssociation"] = (
        capo_cleanrooms.types.configured_table_association.serialize_json(
            value["configured_table_association"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetConfiguredTableAssociationOutput:
    out: GetConfiguredTableAssociationOutput = {}  # type: ignore[typeddict-item]
    if "configuredTableAssociation" in data:
        import capo_cleanrooms.types.configured_table_association

        out["configured_table_association"] = (
            capo_cleanrooms.types.configured_table_association.deserialize_json(
                data["configuredTableAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "GetConfiguredTableAssociationOutput.configured_table_association required"
        )
    return out
