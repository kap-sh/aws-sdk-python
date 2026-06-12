"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipMediaApplicationCall``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.guid_string


class SipMediaApplicationCall(TypedDict):
    transaction_id: NotRequired["aws_sdk_chime_sdk_voice.types.guid_string.GuidString"]
    """<p>The call's transaction ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SipMediaApplicationCall) -> dict:
    out: dict = {}
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    return out


def deserialize_json(data: dict) -> SipMediaApplicationCall:
    out: SipMediaApplicationCall = {}  # type: ignore[typeddict-item]
    if "TransactionId" in data:
        out["transaction_id"] = data["TransactionId"]
    return out
