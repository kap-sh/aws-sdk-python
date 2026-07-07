"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Intent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.confirmation_state
    import aws_sdk_lex_runtime_v2.types.intent_state
    import aws_sdk_lex_runtime_v2.types.non_empty_string
    import aws_sdk_lex_runtime_v2.types.slots


class Intent(TypedDict, closed=True):
    name: "aws_sdk_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    """<p>The name of the intent.</p>"""
    slots: NotRequired["aws_sdk_lex_runtime_v2.types.slots.Slots"]
    """<p>A map of all of the slots for the intent. The name of the slot maps to the value of the slot. If a slot has not been filled, the value is null.</p>"""
    state: NotRequired["aws_sdk_lex_runtime_v2.types.intent_state.IntentState"]
    """<p>Indicates the fulfillment state for the intent. The meanings of each value are as follows:</p> <ul> <li> <p> <code>Failed</code> – The bot failed to fulfill the intent.</p> </li> <li> <p> <code>Fulfilled</code> – The bot has completed fulfillment of the intent.</p> </li> <li> <p> <code>FulfillmentInProgress</code> – The bot is in the middle of fulfilling the intent.</p> </li> <li> <p> <code>InProgress</code> – The bot is in the middle of eliciting the slot values that are necessary to fulfill the intent.</p> </li> <li> <p> <code>ReadyForFulfillment</code> – The bot has elicited all the slot values for the intent and is ready to fulfill the intent.</p> </li> <li> <p> <code>Waiting</code> – The bot is waiting for a response from the user (limited to streaming conversations).</p> </li> </ul>"""
    confirmation_state: NotRequired[
        "aws_sdk_lex_runtime_v2.types.confirmation_state.ConfirmationState"
    ]
    """<p>Indicates whether the intent has been <code>Confirmed</code>, <code>Denied</code>, or <code>None</code> if the confirmation stage has not yet been reached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Intent) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "slots" in value:
        import aws_sdk_lex_runtime_v2.types.slots

        out["slots"] = aws_sdk_lex_runtime_v2.types.slots.serialize_json(value["slots"])
    if "state" in value:
        import aws_sdk_lex_runtime_v2.types.intent_state

        out["state"] = aws_sdk_lex_runtime_v2.types.intent_state.serialize_json(
            value["state"]
        )
    if "confirmation_state" in value:
        import aws_sdk_lex_runtime_v2.types.confirmation_state

        out["confirmationState"] = (
            aws_sdk_lex_runtime_v2.types.confirmation_state.serialize_json(
                value["confirmation_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> Intent:
    out: Intent = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Intent.name required")
    if "slots" in data:
        import aws_sdk_lex_runtime_v2.types.slots

        out["slots"] = aws_sdk_lex_runtime_v2.types.slots.deserialize_json(
            data["slots"]
        )
    if "state" in data:
        import aws_sdk_lex_runtime_v2.types.intent_state

        out["state"] = aws_sdk_lex_runtime_v2.types.intent_state.deserialize_json(
            data["state"]
        )
    if "confirmationState" in data:
        import aws_sdk_lex_runtime_v2.types.confirmation_state

        out["confirmation_state"] = (
            aws_sdk_lex_runtime_v2.types.confirmation_state.deserialize_json(
                data["confirmationState"]
            )
        )
    return out
