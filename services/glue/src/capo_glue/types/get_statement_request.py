"""Generated from Smithy shape ``com.amazonaws.glue#GetStatementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.integer_value
    import capo_glue.types.name_string
    import capo_glue.types.orchestration_name_string


class GetStatementRequest(TypedDict, closed=True):
    session_id: "capo_glue.types.name_string.NameString"
    """<p>The Session ID of the statement.</p>"""
    id: "capo_glue.types.integer_value.IntegerValue"
    """<p>The Id of the statement.</p>"""
    request_origin: NotRequired[
        "capo_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The origin of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetStatementRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    out["Id"] = value.get("id", 0)
    if "request_origin" in value:
        out["RequestOrigin"] = value["request_origin"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetStatementRequest:
    out: GetStatementRequest = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    else:
        raise DeserializationError("GetStatementRequest.session_id required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        out["id"] = 0
    if "RequestOrigin" in data:
        out["request_origin"] = data["RequestOrigin"]
    return out
