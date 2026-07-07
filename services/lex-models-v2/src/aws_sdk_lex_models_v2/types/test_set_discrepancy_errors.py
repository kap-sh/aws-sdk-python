"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetDiscrepancyErrors``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.test_set_intent_discrepancy_list
    import aws_sdk_lex_models_v2.types.test_set_slot_discrepancy_list


class TestSetDiscrepancyErrors(TypedDict, closed=True):
    intent_discrepancies: "aws_sdk_lex_models_v2.types.test_set_intent_discrepancy_list.TestSetIntentDiscrepancyList"
    """<p>Contains information about discrepancies found for intents between the test set and the bot.</p>"""
    slot_discrepancies: "aws_sdk_lex_models_v2.types.test_set_slot_discrepancy_list.TestSetSlotDiscrepancyList"
    """<p>Contains information about discrepancies found for slots between the test set and the bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetDiscrepancyErrors) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.test_set_intent_discrepancy_list

    out["intentDiscrepancies"] = (
        aws_sdk_lex_models_v2.types.test_set_intent_discrepancy_list.serialize_json(
            value["intent_discrepancies"]
        )
    )
    import aws_sdk_lex_models_v2.types.test_set_slot_discrepancy_list

    out["slotDiscrepancies"] = (
        aws_sdk_lex_models_v2.types.test_set_slot_discrepancy_list.serialize_json(
            value["slot_discrepancies"]
        )
    )
    return out


def deserialize_json(data: dict) -> TestSetDiscrepancyErrors:
    out: TestSetDiscrepancyErrors = {}  # type: ignore[typeddict-item]
    if "intentDiscrepancies" in data:
        import aws_sdk_lex_models_v2.types.test_set_intent_discrepancy_list

        out["intent_discrepancies"] = (
            aws_sdk_lex_models_v2.types.test_set_intent_discrepancy_list.deserialize_json(
                data["intentDiscrepancies"]
            )
        )
    else:
        raise DeserializationError(
            "TestSetDiscrepancyErrors.intent_discrepancies required"
        )
    if "slotDiscrepancies" in data:
        import aws_sdk_lex_models_v2.types.test_set_slot_discrepancy_list

        out["slot_discrepancies"] = (
            aws_sdk_lex_models_v2.types.test_set_slot_discrepancy_list.deserialize_json(
                data["slotDiscrepancies"]
            )
        )
    else:
        raise DeserializationError(
            "TestSetDiscrepancyErrors.slot_discrepancies required"
        )
    return out
