"""Generated from Smithy shape ``com.amazonaws.qconnect#ListContentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.content_summary_list
    import aws_sdk_qconnect.types.next_token


class ListContentsResponse(TypedDict):
    content_summaries: "aws_sdk_qconnect.types.content_summary_list.ContentSummaryList"
    """<p>Information about the content.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContentsResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.content_summary_list

    out["contentSummaries"] = (
        aws_sdk_qconnect.types.content_summary_list.serialize_json(
            value["content_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContentsResponse:
    out: ListContentsResponse = {}  # type: ignore[typeddict-item]
    if "contentSummaries" in data:
        import aws_sdk_qconnect.types.content_summary_list

        out["content_summaries"] = (
            aws_sdk_qconnect.types.content_summary_list.deserialize_json(
                data["contentSummaries"]
            )
        )
    else:
        raise DeserializationError("ListContentsResponse.content_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
