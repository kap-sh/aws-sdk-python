"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DeletePublicKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.public_key_arn


class DeletePublicKeyRequest(TypedDict):
    arn: "aws_sdk_ivs_realtime.types.public_key_arn.PublicKeyArn"
    """<p>ARN of the public key to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePublicKeyRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeletePublicKeyRequest:
    out: DeletePublicKeyRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeletePublicKeyRequest.arn required")
    return out
