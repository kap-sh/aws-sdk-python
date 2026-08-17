"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListArchivesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.archive_response_list
    import capo_eventbridge.types.next_token


class ListArchivesResponse(TypedDict, closed=True):
    archives: NotRequired[
        "capo_eventbridge.types.archive_response_list.ArchiveResponseList"
    ]
    """<p>An array of <code>Archive</code> objects that include details about an archive.</p>"""
    next_token: NotRequired["capo_eventbridge.types.next_token.NextToken"]
    """<p>A token indicating there are more results available. If there are no more results, no token is included in the response.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListArchivesResponse) -> dict:
    out: dict = {}
    if "archives" in value:
        import capo_eventbridge.types.archive_response_list

        out["Archives"] = (
            capo_eventbridge.types.archive_response_list.serialize_aws_json_1_1(
                value["archives"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListArchivesResponse:
    out: ListArchivesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Archives") is not None:
        import capo_eventbridge.types.archive_response_list

        out["archives"] = (
            capo_eventbridge.types.archive_response_list.deserialize_aws_json_1_1(
                data["Archives"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
