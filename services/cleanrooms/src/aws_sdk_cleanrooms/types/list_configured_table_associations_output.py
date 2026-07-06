"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListConfiguredTableAssociationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_association_summary_list
    import aws_sdk_cleanrooms.types.pagination_token


class ListConfiguredTableAssociationsOutput(TypedDict, closed=True):
    configured_table_association_summaries: "aws_sdk_cleanrooms.types.configured_table_association_summary_list.ConfiguredTableAssociationSummaryList"
    """<p>The retrieved list of configured table associations.</p>"""
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfiguredTableAssociationsOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.configured_table_association_summary_list

    out["configuredTableAssociationSummaries"] = (
        aws_sdk_cleanrooms.types.configured_table_association_summary_list.serialize_json(
            value["configured_table_association_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfiguredTableAssociationsOutput:
    out: ListConfiguredTableAssociationsOutput = {}  # type: ignore[typeddict-item]
    if "configuredTableAssociationSummaries" in data:
        import aws_sdk_cleanrooms.types.configured_table_association_summary_list

        out["configured_table_association_summaries"] = (
            aws_sdk_cleanrooms.types.configured_table_association_summary_list.deserialize_json(
                data["configuredTableAssociationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListConfiguredTableAssociationsOutput.configured_table_association_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
