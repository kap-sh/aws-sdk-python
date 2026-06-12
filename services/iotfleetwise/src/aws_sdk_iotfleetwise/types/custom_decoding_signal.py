"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CustomDecodingSignal``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.custom_decoding_id


class CustomDecodingSignal(TypedDict):
    id: "aws_sdk_iotfleetwise.types.custom_decoding_id.CustomDecodingId"
    """<p>The ID of the signal.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomDecodingSignal) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomDecodingSignal:
    out: CustomDecodingSignal = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CustomDecodingSignal.id required")
    return out
