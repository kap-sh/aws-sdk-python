"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#IntentSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_runtime_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_service.types.confirmation_status
    import aws_sdk_lex_runtime_service.types.dialog_action_type
    import aws_sdk_lex_runtime_service.types.fulfillment_state
    import aws_sdk_lex_runtime_service.types.intent_name
    import aws_sdk_lex_runtime_service.types.intent_summary_checkpoint_label
    import aws_sdk_lex_runtime_service.types.string
    import aws_sdk_lex_runtime_service.types.string_map


class IntentSummary(TypedDict):
    intent_name: NotRequired["aws_sdk_lex_runtime_service.types.intent_name.IntentName"]
    """<p>The name of the intent.</p>"""
    checkpoint_label: NotRequired[
        "aws_sdk_lex_runtime_service.types.intent_summary_checkpoint_label.IntentSummaryCheckpointLabel"
    ]
    """<p>A user-defined label that identifies a particular intent. You can use this label to return to a previous intent. </p> <p>Use the <code>checkpointLabelFilter</code> parameter of the <code>GetSessionRequest</code> operation to filter the intents returned by the operation to those with only the specified label.</p>"""
    slots: NotRequired["aws_sdk_lex_runtime_service.types.string_map.StringMap"]
    """<p>Map of the slots that have been gathered and their values. </p>"""
    confirmation_status: NotRequired[
        "aws_sdk_lex_runtime_service.types.confirmation_status.ConfirmationStatus"
    ]
    r"""<p>The status of the intent after the user responds to the confirmation prompt. If the user confirms the intent, Amazon Lex sets this field to <code>Confirmed</code>. If the user denies the intent, Amazon Lex sets this value to <code>Denied</code>. The possible values are:</p> <ul> <li> <p> <code>Confirmed</code> - The user has responded \"Yes\" to the confirmation prompt, confirming that the intent is complete and that it is ready to be fulfilled.</p> </li> <li> <p> <code>Denied</code> - The user has responded \"No\" to the confirmation prompt.</p> </li> <li> <p> <code>None</code> - The user has never been prompted for confirmation; or, the user was prompted but did not confirm or deny the prompt.</p> </li> </ul>"""
    dialog_action_type: (
        "aws_sdk_lex_runtime_service.types.dialog_action_type.DialogActionType"
    )
    r"""<p>The next action that the bot should take in its interaction with the user. The possible values are:</p> <ul> <li> <p> <code>ConfirmIntent</code> - The next action is asking the user if the intent is complete and ready to be fulfilled. This is a yes/no question such as \"Place the order?\"</p> </li> <li> <p> <code>Close</code> - Indicates that the there will not be a response from the user. For example, the statement \"Your order has been placed\" does not require a response.</p> </li> <li> <p> <code>ElicitIntent</code> - The next action is to determine the intent that the user wants to fulfill.</p> </li> <li> <p> <code>ElicitSlot</code> - The next action is to elicit a slot value from the user.</p> </li> </ul>"""
    fulfillment_state: NotRequired[
        "aws_sdk_lex_runtime_service.types.fulfillment_state.FulfillmentState"
    ]
    """<p>The fulfillment state of the intent. The possible values are:</p> <ul> <li> <p> <code>Failed</code> - The Lambda function associated with the intent failed to fulfill the intent.</p> </li> <li> <p> <code>Fulfilled</code> - The intent has fulfilled by the Lambda function associated with the intent. </p> </li> <li> <p> <code>ReadyForFulfillment</code> - All of the information necessary for the intent is present and the intent ready to be fulfilled by the client application.</p> </li> </ul>"""
    slot_to_elicit: NotRequired["aws_sdk_lex_runtime_service.types.string.String"]
    """<p>The next slot to elicit from the user. If there is not slot to elicit, the field is blank.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentSummary) -> dict:
    out: dict = {}
    if "intent_name" in value:
        out["intentName"] = value["intent_name"]
    if "checkpoint_label" in value:
        out["checkpointLabel"] = value["checkpoint_label"]
    if "slots" in value:
        import aws_sdk_lex_runtime_service.types.string_map

        out["slots"] = aws_sdk_lex_runtime_service.types.string_map.serialize_json(
            value["slots"]
        )
    if "confirmation_status" in value:
        import aws_sdk_lex_runtime_service.types.confirmation_status

        out["confirmationStatus"] = (
            aws_sdk_lex_runtime_service.types.confirmation_status.serialize_json(
                value["confirmation_status"]
            )
        )
    import aws_sdk_lex_runtime_service.types.dialog_action_type

    out["dialogActionType"] = (
        aws_sdk_lex_runtime_service.types.dialog_action_type.serialize_json(
            value["dialog_action_type"]
        )
    )
    if "fulfillment_state" in value:
        import aws_sdk_lex_runtime_service.types.fulfillment_state

        out["fulfillmentState"] = (
            aws_sdk_lex_runtime_service.types.fulfillment_state.serialize_json(
                value["fulfillment_state"]
            )
        )
    if "slot_to_elicit" in value:
        out["slotToElicit"] = value["slot_to_elicit"]
    return out


def deserialize_json(data: dict) -> IntentSummary:
    out: IntentSummary = {}  # type: ignore[typeddict-item]
    if "intentName" in data:
        out["intent_name"] = data["intentName"]
    if "checkpointLabel" in data:
        out["checkpoint_label"] = data["checkpointLabel"]
    if "slots" in data:
        import aws_sdk_lex_runtime_service.types.string_map

        out["slots"] = aws_sdk_lex_runtime_service.types.string_map.deserialize_json(
            data["slots"]
        )
    if "confirmationStatus" in data:
        import aws_sdk_lex_runtime_service.types.confirmation_status

        out["confirmation_status"] = (
            aws_sdk_lex_runtime_service.types.confirmation_status.deserialize_json(
                data["confirmationStatus"]
            )
        )
    if "dialogActionType" in data:
        import aws_sdk_lex_runtime_service.types.dialog_action_type

        out["dialog_action_type"] = (
            aws_sdk_lex_runtime_service.types.dialog_action_type.deserialize_json(
                data["dialogActionType"]
            )
        )
    else:
        raise DeserializationError("IntentSummary.dialog_action_type required")
    if "fulfillmentState" in data:
        import aws_sdk_lex_runtime_service.types.fulfillment_state

        out["fulfillment_state"] = (
            aws_sdk_lex_runtime_service.types.fulfillment_state.deserialize_json(
                data["fulfillmentState"]
            )
        )
    if "slotToElicit" in data:
        out["slot_to_elicit"] = data["slotToElicit"]
    return out
