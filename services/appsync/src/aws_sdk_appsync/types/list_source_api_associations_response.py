"""Generated from Smithy shape ``com.amazonaws.appsync#ListSourceApiAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.pagination_token
    import aws_sdk_appsync.types.source_api_association_summary_list


class ListSourceApiAssociationsResponse(TypedDict):
    source_api_association_summaries: NotRequired[
        "aws_sdk_appsync.types.source_api_association_summary_list.SourceApiAssociationSummaryList"
    ]
    """<p>The <code>SourceApiAssociationSummary</code> object data.</p>"""
    next_token: NotRequired["aws_sdk_appsync.types.pagination_token.PaginationToken"]
    """<p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceApiAssociationsResponse) -> dict:
    out: dict = {}
    if "source_api_association_summaries" in value:
        import aws_sdk_appsync.types.source_api_association_summary_list

        out["sourceApiAssociationSummaries"] = (
            aws_sdk_appsync.types.source_api_association_summary_list.serialize_json(
                value["source_api_association_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSourceApiAssociationsResponse:
    out: ListSourceApiAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "sourceApiAssociationSummaries" in data:
        import aws_sdk_appsync.types.source_api_association_summary_list

        out["source_api_association_summaries"] = (
            aws_sdk_appsync.types.source_api_association_summary_list.deserialize_json(
                data["sourceApiAssociationSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
