"""Generated from Smithy shape ``com.amazonaws.glue#StopSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.orchestration_name_string


class StopSessionRequest(TypedDict, closed=True):
    id: "aws_sdk_glue.types.name_string.NameString"
    """<p>The ID of the session to be stopped.</p>"""
    request_origin: NotRequired[
        "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The origin of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopSessionRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "request_origin" in value:
        out["RequestOrigin"] = value["request_origin"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopSessionRequest:
    out: StopSessionRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("StopSessionRequest.id required")
    if "RequestOrigin" in data:
        out["request_origin"] = data["RequestOrigin"]
    return out
