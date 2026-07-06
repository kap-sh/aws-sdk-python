"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateIdMappingTableOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.id_mapping_table


class CreateIdMappingTableOutput(TypedDict, closed=True):
    id_mapping_table: "aws_sdk_cleanrooms.types.id_mapping_table.IdMappingTable"
    """<p>The ID mapping table that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIdMappingTableOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.id_mapping_table

    out["idMappingTable"] = aws_sdk_cleanrooms.types.id_mapping_table.serialize_json(
        value["id_mapping_table"]
    )
    return out


def deserialize_json(data: dict) -> CreateIdMappingTableOutput:
    out: CreateIdMappingTableOutput = {}  # type: ignore[typeddict-item]
    if "idMappingTable" in data:
        import aws_sdk_cleanrooms.types.id_mapping_table

        out["id_mapping_table"] = (
            aws_sdk_cleanrooms.types.id_mapping_table.deserialize_json(
                data["idMappingTable"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIdMappingTableOutput.id_mapping_table required"
        )
    return out
