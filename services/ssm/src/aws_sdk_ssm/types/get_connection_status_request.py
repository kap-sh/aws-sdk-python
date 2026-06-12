"""Generated from Smithy shape ``com.amazonaws.ssm#GetConnectionStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.session_target


class GetConnectionStatusRequest(TypedDict):
    target: "aws_sdk_ssm.types.session_target.SessionTarget"
    """<p>The managed node ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConnectionStatusRequest) -> dict:
    out: dict = {}
    out["Target"] = value["target"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConnectionStatusRequest:
    out: GetConnectionStatusRequest = {}  # type: ignore[typeddict-item]
    if "Target" in data:
        out["target"] = data["Target"]
    else:
        raise DeserializationError("GetConnectionStatusRequest.target required")
    return out
