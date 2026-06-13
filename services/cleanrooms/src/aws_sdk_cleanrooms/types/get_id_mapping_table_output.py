"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetIdMappingTableOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.id_mapping_table


class GetIdMappingTableOutput(TypedDict):
    id_mapping_table: "aws_sdk_cleanrooms.types.id_mapping_table.IdMappingTable"
    """<p>The ID mapping table that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdMappingTableOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.id_mapping_table

    out["idMappingTable"] = aws_sdk_cleanrooms.types.id_mapping_table.serialize_json(
        value["id_mapping_table"]
    )
    return out


def deserialize_json(data: dict) -> GetIdMappingTableOutput:
    out: GetIdMappingTableOutput = {}  # type: ignore[typeddict-item]
    if "idMappingTable" in data:
        import aws_sdk_cleanrooms.types.id_mapping_table

        out["id_mapping_table"] = (
            aws_sdk_cleanrooms.types.id_mapping_table.deserialize_json(
                data["idMappingTable"]
            )
        )
    else:
        raise DeserializationError("GetIdMappingTableOutput.id_mapping_table required")
    return out
