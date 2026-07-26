"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateIdMappingTableOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.id_mapping_table


class UpdateIdMappingTableOutput(TypedDict, closed=True):
    id_mapping_table: "capo_cleanrooms.types.id_mapping_table.IdMappingTable"
    """<p>The updated ID mapping table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIdMappingTableOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.id_mapping_table

    out["idMappingTable"] = capo_cleanrooms.types.id_mapping_table.serialize_json(
        value["id_mapping_table"]
    )
    return out


def deserialize_json(data: dict) -> UpdateIdMappingTableOutput:
    out: UpdateIdMappingTableOutput = {}  # type: ignore[typeddict-item]
    if "idMappingTable" in data:
        import capo_cleanrooms.types.id_mapping_table

        out["id_mapping_table"] = (
            capo_cleanrooms.types.id_mapping_table.deserialize_json(
                data["idMappingTable"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIdMappingTableOutput.id_mapping_table required"
        )
    return out
