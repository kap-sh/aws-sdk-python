"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListIdMappingTablesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.id_mapping_table_summary_list
    import aws_sdk_cleanrooms.types.pagination_token


class ListIdMappingTablesOutput(TypedDict):
    id_mapping_table_summaries: "aws_sdk_cleanrooms.types.id_mapping_table_summary_list.IdMappingTableSummaryList"
    """<p>The summary information of the ID mapping tables that you requested.</p>"""
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The token value provided to access the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdMappingTablesOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.id_mapping_table_summary_list

    out["idMappingTableSummaries"] = (
        aws_sdk_cleanrooms.types.id_mapping_table_summary_list.serialize_json(
            value["id_mapping_table_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIdMappingTablesOutput:
    out: ListIdMappingTablesOutput = {}  # type: ignore[typeddict-item]
    if "idMappingTableSummaries" in data:
        import aws_sdk_cleanrooms.types.id_mapping_table_summary_list

        out["id_mapping_table_summaries"] = (
            aws_sdk_cleanrooms.types.id_mapping_table_summary_list.deserialize_json(
                data["idMappingTableSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListIdMappingTablesOutput.id_mapping_table_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
