"""Generated from Smithy shape ``com.amazonaws.glue#RunStatementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.orchestration_name_string
    import aws_sdk_glue.types.orchestration_statement_code_string


class RunStatementRequest(TypedDict, closed=True):
    session_id: "aws_sdk_glue.types.name_string.NameString"
    """<p>The Session Id of the statement to be run.</p>"""
    code: "aws_sdk_glue.types.orchestration_statement_code_string.OrchestrationStatementCodeString"
    """<p>The statement code to be run.</p>"""
    request_origin: NotRequired[
        "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The origin of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunStatementRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    out["Code"] = value["code"]
    if "request_origin" in value:
        out["RequestOrigin"] = value["request_origin"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RunStatementRequest:
    out: RunStatementRequest = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    else:
        raise DeserializationError("RunStatementRequest.session_id required")
    if "Code" in data:
        out["code"] = data["Code"]
    else:
        raise DeserializationError("RunStatementRequest.code required")
    if "RequestOrigin" in data:
        out["request_origin"] = data["RequestOrigin"]
    return out
