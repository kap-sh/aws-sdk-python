"""Generated from Smithy shape ``com.amazonaws.mturk#GetHITRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.entity_id


class GetHITRequest(TypedDict):
    hit_id: "aws_sdk_mturk.types.entity_id.EntityId"
    """<p>The ID of the HIT to be retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetHITRequest) -> dict:
    out: dict = {}
    out["HITId"] = value["hit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetHITRequest:
    out: GetHITRequest = {}  # type: ignore[typeddict-item]
    if "HITId" in data:
        out["hit_id"] = data["HITId"]
    else:
        raise DeserializationError("GetHITRequest.hit_id required")
    return out
