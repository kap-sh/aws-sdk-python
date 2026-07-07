"""Generated from Smithy shape ``com.amazonaws.qbusiness#SearchRelevantContentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.next_token
    import aws_sdk_qbusiness.types.relevant_content_list


class SearchRelevantContentResponse(TypedDict, closed=True):
    relevant_content: NotRequired[
        "aws_sdk_qbusiness.types.relevant_content_list.RelevantContentList"
    ]
    """<p>The list of relevant content items found.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next set of results, if there are any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRelevantContentResponse) -> dict:
    out: dict = {}
    if "relevant_content" in value:
        import aws_sdk_qbusiness.types.relevant_content_list

        out["relevantContent"] = (
            aws_sdk_qbusiness.types.relevant_content_list.serialize_json(
                value["relevant_content"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchRelevantContentResponse:
    out: SearchRelevantContentResponse = {}  # type: ignore[typeddict-item]
    if "relevantContent" in data:
        import aws_sdk_qbusiness.types.relevant_content_list

        out["relevant_content"] = (
            aws_sdk_qbusiness.types.relevant_content_list.deserialize_json(
                data["relevantContent"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
