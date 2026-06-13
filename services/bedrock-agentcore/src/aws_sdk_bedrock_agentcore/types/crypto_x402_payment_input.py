"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CryptoX402PaymentInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.payment_document

class CryptoX402PaymentInput(TypedDict):
    version: "str"
    """<p>The version of the X402 protocol.</p>"""
    payload: "aws_sdk_bedrock_agentcore.types.payment_document.PaymentDocument"
    """<p>The X402 payment payload.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CryptoX402PaymentInput) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    out["payload"] = value["payload"]
    return out


def deserialize_json(data: dict) -> CryptoX402PaymentInput:
    out: CryptoX402PaymentInput = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CryptoX402PaymentInput.version required")
    if "payload" in data:
        out["payload"] = data["payload"]
    else:
        raise DeserializationError("CryptoX402PaymentInput.payload required")
    return out