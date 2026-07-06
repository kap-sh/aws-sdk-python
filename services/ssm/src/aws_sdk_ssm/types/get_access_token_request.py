"""Generated from Smithy shape ``com.amazonaws.ssm#GetAccessTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.access_request_id


class GetAccessTokenRequest(TypedDict, closed=True):
    access_request_id: "aws_sdk_ssm.types.access_request_id.AccessRequestId"
    """<p>The ID of a just-in-time node access request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccessTokenRequest) -> dict:
    out: dict = {}
    out["AccessRequestId"] = value["access_request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccessTokenRequest:
    out: GetAccessTokenRequest = {}  # type: ignore[typeddict-item]
    if "AccessRequestId" in data:
        out["access_request_id"] = data["AccessRequestId"]
    else:
        raise DeserializationError("GetAccessTokenRequest.access_request_id required")
    return out
