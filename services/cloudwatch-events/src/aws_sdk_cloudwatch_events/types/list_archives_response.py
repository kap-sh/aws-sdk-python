"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListArchivesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.archive_response_list
    import aws_sdk_cloudwatch_events.types.next_token


class ListArchivesResponse(TypedDict):
    archives: NotRequired[
        "aws_sdk_cloudwatch_events.types.archive_response_list.ArchiveResponseList"
    ]
    """<p>An array of <code>Archive</code> objects that include details about an archive.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_events.types.next_token.NextToken"]
    """<p>The token returned by a previous call to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListArchivesResponse) -> dict:
    out: dict = {}
    if "archives" in value:
        import aws_sdk_cloudwatch_events.types.archive_response_list

        out["Archives"] = (
            aws_sdk_cloudwatch_events.types.archive_response_list.serialize_aws_json_1_1(
                value["archives"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListArchivesResponse:
    out: ListArchivesResponse = {}  # type: ignore[typeddict-item]
    if "Archives" in data:
        import aws_sdk_cloudwatch_events.types.archive_response_list

        out["archives"] = (
            aws_sdk_cloudwatch_events.types.archive_response_list.deserialize_aws_json_1_1(
                data["Archives"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
