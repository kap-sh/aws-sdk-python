"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeSessionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.session_list
    import aws_sdk_appstream.types.string


class DescribeSessionsResult(TypedDict, closed=True):
    sessions: NotRequired["aws_sdk_appstream.types.session_list.SessionList"]
    """<p>Information about the streaming sessions.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSessionsResult) -> dict:
    out: dict = {}
    if "sessions" in value:
        import aws_sdk_appstream.types.session_list

        out["Sessions"] = aws_sdk_appstream.types.session_list.serialize_aws_json_1_1(
            value["sessions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSessionsResult:
    out: DescribeSessionsResult = {}  # type: ignore[typeddict-item]
    if "Sessions" in data:
        import aws_sdk_appstream.types.session_list

        out["sessions"] = aws_sdk_appstream.types.session_list.deserialize_aws_json_1_1(
            data["Sessions"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
