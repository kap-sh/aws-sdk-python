"""Generated from Smithy shape ``com.amazonaws.quicksight#DestinationTable``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.destination_table_alias
    import aws_sdk_quicksight.types.destination_table_source


class DestinationTable(TypedDict, closed=True):
    alias: "aws_sdk_quicksight.types.destination_table_alias.DestinationTableAlias"
    """<p>Alias for the destination table.</p>"""
    source: "aws_sdk_quicksight.types.destination_table_source.DestinationTableSource"
    """<p>The source configuration that specifies which transform operation provides data to this destination table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationTable) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import aws_sdk_quicksight.types.destination_table_source

    out["Source"] = aws_sdk_quicksight.types.destination_table_source.serialize_json(
        value["source"]
    )
    return out


def deserialize_json(data: dict) -> DestinationTable:
    out: DestinationTable = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("DestinationTable.alias required")
    if "Source" in data:
        import aws_sdk_quicksight.types.destination_table_source

        out["source"] = (
            aws_sdk_quicksight.types.destination_table_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("DestinationTable.source required")
    return out
