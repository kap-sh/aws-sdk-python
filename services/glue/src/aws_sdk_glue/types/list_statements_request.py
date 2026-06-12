"""Generated from Smithy shape ``com.amazonaws.glue#ListStatementsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.orchestration_name_string
    import aws_sdk_glue.types.orchestration_token


class ListStatementsRequest(TypedDict):
    session_id: "aws_sdk_glue.types.name_string.NameString"
    """<p>The Session ID of the statements.</p>"""
    request_origin: NotRequired[
        "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The origin of the request to list statements.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.orchestration_token.OrchestrationToken"]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStatementsRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    if "request_origin" in value:
        out["RequestOrigin"] = value["request_origin"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStatementsRequest:
    out: ListStatementsRequest = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    else:
        raise DeserializationError("ListStatementsRequest.session_id required")
    if "RequestOrigin" in data:
        out["request_origin"] = data["RequestOrigin"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
