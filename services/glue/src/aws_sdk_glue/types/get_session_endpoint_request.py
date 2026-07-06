"""Generated from Smithy shape ``com.amazonaws.glue#GetSessionEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class GetSessionEndpointRequest(TypedDict, closed=True):
    session_id: "aws_sdk_glue.types.name_string.NameString"
    """<p>The unique identifier of the interactive session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSessionEndpointRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSessionEndpointRequest:
    out: GetSessionEndpointRequest = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    else:
        raise DeserializationError("GetSessionEndpointRequest.session_id required")
    return out
