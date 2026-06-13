"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListSchemasOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.pagination_token
    import aws_sdk_cleanrooms.types.schema_summary_list


class ListSchemasOutput(TypedDict):
    schema_summaries: "aws_sdk_cleanrooms.types.schema_summary_list.SchemaSummaryList"
    """<p>The retrieved list of schemas.</p>"""
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchemasOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.schema_summary_list

    out["schemaSummaries"] = (
        aws_sdk_cleanrooms.types.schema_summary_list.serialize_json(
            value["schema_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSchemasOutput:
    out: ListSchemasOutput = {}  # type: ignore[typeddict-item]
    if "schemaSummaries" in data:
        import aws_sdk_cleanrooms.types.schema_summary_list

        out["schema_summaries"] = (
            aws_sdk_cleanrooms.types.schema_summary_list.deserialize_json(
                data["schemaSummaries"]
            )
        )
    else:
        raise DeserializationError("ListSchemasOutput.schema_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
