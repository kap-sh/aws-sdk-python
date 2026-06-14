"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LinkedAccountSms``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.phone_number


class LinkedAccountSms(TypedDict):
    phone_number: "aws_sdk_bedrock_agentcore.types.phone_number.PhoneNumber"
    """<p>The phone number in E.164 format (e.g., +1234567890).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkedAccountSms) -> dict:
    out: dict = {}
    out["phoneNumber"] = value["phone_number"]
    return out


def deserialize_json(data: dict) -> LinkedAccountSms:
    out: LinkedAccountSms = {}  # type: ignore[typeddict-item]
    if "phoneNumber" in data:
        out["phone_number"] = data["phoneNumber"]
    else:
        raise DeserializationError("LinkedAccountSms.phone_number required")
    return out
