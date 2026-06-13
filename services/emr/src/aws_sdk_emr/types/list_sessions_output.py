"""Generated from Smithy shape ``com.amazonaws.emr#ListSessionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.session_list
    import aws_sdk_emr.types.string


class ListSessionsOutput(TypedDict):
    sessions: NotRequired["aws_sdk_emr.types.session_list.SessionList"]
    """<p>The sessions that match the request.</p>"""
    next_token: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The pagination token to use in a subsequent <code>ListSessions</code> call to retrieve the next page of results. This field is absent when there are no more results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSessionsOutput) -> dict:
    out: dict = {}
    if "sessions" in value:
        import aws_sdk_emr.types.session_list

        out["Sessions"] = aws_sdk_emr.types.session_list.serialize_aws_json_1_1(
            value["sessions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSessionsOutput:
    out: ListSessionsOutput = {}  # type: ignore[typeddict-item]
    if "Sessions" in data:
        import aws_sdk_emr.types.session_list

        out["sessions"] = aws_sdk_emr.types.session_list.deserialize_aws_json_1_1(
            data["Sessions"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
