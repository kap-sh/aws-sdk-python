"""Generated from Smithy shape ``com.amazonaws.qconnect#ListContentAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.content_association_summary_list
    import aws_sdk_qconnect.types.next_token


class ListContentAssociationsResponse(TypedDict):
    content_association_summaries: "aws_sdk_qconnect.types.content_association_summary_list.ContentAssociationSummaryList"
    """<p>Summary information about content associations.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContentAssociationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.content_association_summary_list

    out["contentAssociationSummaries"] = (
        aws_sdk_qconnect.types.content_association_summary_list.serialize_json(
            value["content_association_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContentAssociationsResponse:
    out: ListContentAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "contentAssociationSummaries" in data:
        import aws_sdk_qconnect.types.content_association_summary_list

        out["content_association_summaries"] = (
            aws_sdk_qconnect.types.content_association_summary_list.deserialize_json(
                data["contentAssociationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListContentAssociationsResponse.content_association_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
