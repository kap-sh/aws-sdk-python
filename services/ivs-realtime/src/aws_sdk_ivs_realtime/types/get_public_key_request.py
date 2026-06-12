"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetPublicKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.public_key_arn


class GetPublicKeyRequest(TypedDict):
    arn: "aws_sdk_ivs_realtime.types.public_key_arn.PublicKeyArn"
    """<p>ARN of the public key for which the information is to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPublicKeyRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetPublicKeyRequest:
    out: GetPublicKeyRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetPublicKeyRequest.arn required")
    return out
