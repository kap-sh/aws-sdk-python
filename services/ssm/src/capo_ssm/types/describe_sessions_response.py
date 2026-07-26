"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.session_list


class DescribeSessionsResponse(TypedDict, closed=True):
    sessions: NotRequired["capo_ssm.types.session_list.SessionList"]
    """<p>A list of sessions meeting the request parameters.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSessionsResponse) -> dict:
    out: dict = {}
    if "sessions" in value:
        import capo_ssm.types.session_list

        out["Sessions"] = capo_ssm.types.session_list.serialize_aws_json_1_1(
            value["sessions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSessionsResponse:
    out: DescribeSessionsResponse = {}  # type: ignore[typeddict-item]
    if "Sessions" in data:
        import capo_ssm.types.session_list

        out["sessions"] = capo_ssm.types.session_list.deserialize_aws_json_1_1(
            data["Sessions"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
