"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListConfiguredTablesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_summary_list
    import aws_sdk_cleanrooms.types.pagination_token


class ListConfiguredTablesOutput(TypedDict, closed=True):
    configured_table_summaries: "aws_sdk_cleanrooms.types.configured_table_summary_list.ConfiguredTableSummaryList"
    """<p>The configured tables listed by the request.</p>"""
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfiguredTablesOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.configured_table_summary_list

    out["configuredTableSummaries"] = (
        aws_sdk_cleanrooms.types.configured_table_summary_list.serialize_json(
            value["configured_table_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfiguredTablesOutput:
    out: ListConfiguredTablesOutput = {}  # type: ignore[typeddict-item]
    if "configuredTableSummaries" in data:
        import aws_sdk_cleanrooms.types.configured_table_summary_list

        out["configured_table_summaries"] = (
            aws_sdk_cleanrooms.types.configured_table_summary_list.deserialize_json(
                data["configuredTableSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListConfiguredTablesOutput.configured_table_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
