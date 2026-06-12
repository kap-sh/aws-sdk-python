"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetSlotDiscrepancyItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.string


class TestSetSlotDiscrepancyItem(TypedDict):
    intent_name: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The name of the intent associated with the slot in the discrepancy report.</p>"""
    slot_name: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The name of the slot in the discrepancy report.</p>"""
    error_message: "aws_sdk_lex_models_v2.types.string.String"
    """<p>The error message for a discrepancy for an intent between the test set and the bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetSlotDiscrepancyItem) -> dict:
    out: dict = {}
    out["intentName"] = value["intent_name"]
    out["slotName"] = value["slot_name"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> TestSetSlotDiscrepancyItem:
    out: TestSetSlotDiscrepancyItem = {}  # type: ignore[typeddict-item]
    if "intentName" in data:
        out["intent_name"] = data["intentName"]
    else:
        raise DeserializationError("TestSetSlotDiscrepancyItem.intent_name required")
    if "slotName" in data:
        out["slot_name"] = data["slotName"]
    else:
        raise DeserializationError("TestSetSlotDiscrepancyItem.slot_name required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError("TestSetSlotDiscrepancyItem.error_message required")
    return out
