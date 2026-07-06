"""Generated from Smithy shape ``com.amazonaws.ivs#GetStreamKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.stream_key_arn


class GetStreamKeyRequest(TypedDict, closed=True):
    arn: "aws_sdk_ivs.types.stream_key_arn.StreamKeyArn"
    """<p>ARN for the stream key to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamKeyRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetStreamKeyRequest:
    out: GetStreamKeyRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetStreamKeyRequest.arn required")
    return out
