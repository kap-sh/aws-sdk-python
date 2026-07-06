"""Generated from Smithy shape ``com.amazonaws.glue#ListSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.orchestration_token
    import aws_sdk_glue.types.session_id_list
    import aws_sdk_glue.types.session_list


class ListSessionsResponse(TypedDict, closed=True):
    ids: NotRequired["aws_sdk_glue.types.session_id_list.SessionIdList"]
    """<p>Returns the ID of the session. </p>"""
    sessions: NotRequired["aws_sdk_glue.types.session_list.SessionList"]
    """<p>Returns the session object. </p>"""
    next_token: NotRequired["aws_sdk_glue.types.orchestration_token.OrchestrationToken"]
    """<p>The token for the next set of results, or null if there are no more result. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSessionsResponse) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_glue.types.session_id_list

        out["Ids"] = aws_sdk_glue.types.session_id_list.serialize_aws_json_1_1(
            value["ids"]
        )
    if "sessions" in value:
        import aws_sdk_glue.types.session_list

        out["Sessions"] = aws_sdk_glue.types.session_list.serialize_aws_json_1_1(
            value["sessions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSessionsResponse:
    out: ListSessionsResponse = {}  # type: ignore[typeddict-item]
    if "Ids" in data:
        import aws_sdk_glue.types.session_id_list

        out["ids"] = aws_sdk_glue.types.session_id_list.deserialize_aws_json_1_1(
            data["Ids"]
        )
    if "Sessions" in data:
        import aws_sdk_glue.types.session_list

        out["sessions"] = aws_sdk_glue.types.session_list.deserialize_aws_json_1_1(
            data["Sessions"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
