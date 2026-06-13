"""Generated from Smithy shape ``com.amazonaws.ssmincidents#RegionMapInputValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.sse_kms_key


class RegionMapInputValue(TypedDict):
    sse_kms_key_id: NotRequired["aws_sdk_ssm_incidents.types.sse_kms_key.SseKmsKey"]
    """<p>The KMS key used to encrypt the data in your replication set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegionMapInputValue) -> dict:
    out: dict = {}
    if "sse_kms_key_id" in value:
        out["sseKmsKeyId"] = value["sse_kms_key_id"]
    return out


def deserialize_json(data: dict) -> RegionMapInputValue:
    out: RegionMapInputValue = {}  # type: ignore[typeddict-item]
    if "sseKmsKeyId" in data:
        out["sse_kms_key_id"] = data["sseKmsKeyId"]
    return out
