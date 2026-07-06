"""Generated from Smithy shape ``com.amazonaws.glue#CancelStatementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.integer_value
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.orchestration_name_string


class CancelStatementRequest(TypedDict, closed=True):
    session_id: "aws_sdk_glue.types.name_string.NameString"
    """<p>The Session ID of the statement to be cancelled.</p>"""
    id: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>The ID of the statement to be cancelled.</p>"""
    request_origin: NotRequired[
        "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The origin of the request to cancel the statement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelStatementRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    out["Id"] = value.get("id", 0)
    if "request_origin" in value:
        out["RequestOrigin"] = value["request_origin"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelStatementRequest:
    out: CancelStatementRequest = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    else:
        raise DeserializationError("CancelStatementRequest.session_id required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        out["id"] = 0
    if "RequestOrigin" in data:
        out["request_origin"] = data["RequestOrigin"]
    return out
