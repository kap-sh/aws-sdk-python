"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.display_name
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.input_contexts_list
    import capo_lex_models_v2.types.intent_signature
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.output_contexts_list
    import capo_lex_models_v2.types.timestamp


class IntentSummary(TypedDict, closed=True):
    intent_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier assigned to the intent. Use this ID to get detailed information about the intent with the <code>DescribeIntent</code> operation.</p>"""
    intent_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The name of the intent.</p>"""
    intent_display_name: NotRequired[
        "capo_lex_models_v2.types.display_name.DisplayName"
    ]
    """<p>The display name of the intent.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The description of the intent.</p>"""
    parent_intent_signature: NotRequired[
        "capo_lex_models_v2.types.intent_signature.IntentSignature"
    ]
    """<p>If this intent is derived from a built-in intent, the name of the parent intent.</p>"""
    input_contexts: NotRequired[
        "capo_lex_models_v2.types.input_contexts_list.InputContextsList"
    ]
    """<p>The input contexts that must be active for this intent to be considered for recognition.</p>"""
    output_contexts: NotRequired[
        "capo_lex_models_v2.types.output_contexts_list.OutputContextsList"
    ]
    """<p>The output contexts that are activated when this intent is fulfilled.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The timestamp of the date and time that the intent was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentSummary) -> dict:
    out: dict = {}
    if "intent_id" in value:
        out["intentId"] = value["intent_id"]
    if "intent_name" in value:
        out["intentName"] = value["intent_name"]
    if "intent_display_name" in value:
        out["intentDisplayName"] = value["intent_display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "parent_intent_signature" in value:
        out["parentIntentSignature"] = value["parent_intent_signature"]
    if "input_contexts" in value:
        import capo_lex_models_v2.types.input_contexts_list

        out["inputContexts"] = (
            capo_lex_models_v2.types.input_contexts_list.serialize_json(
                value["input_contexts"]
            )
        )
    if "output_contexts" in value:
        import capo_lex_models_v2.types.output_contexts_list

        out["outputContexts"] = (
            capo_lex_models_v2.types.output_contexts_list.serialize_json(
                value["output_contexts"]
            )
        )
    if "last_updated_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["last_updated_date_time"]
        )
    return out


def deserialize_json(data: dict) -> IntentSummary:
    out: IntentSummary = {}  # type: ignore[typeddict-item]
    if "intentId" in data:
        out["intent_id"] = data["intentId"]
    if "intentName" in data:
        out["intent_name"] = data["intentName"]
    if "intentDisplayName" in data:
        out["intent_display_name"] = data["intentDisplayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "parentIntentSignature" in data:
        out["parent_intent_signature"] = data["parentIntentSignature"]
    if "inputContexts" in data:
        import capo_lex_models_v2.types.input_contexts_list

        out["input_contexts"] = (
            capo_lex_models_v2.types.input_contexts_list.deserialize_json(
                data["inputContexts"]
            )
        )
    if "outputContexts" in data:
        import capo_lex_models_v2.types.output_contexts_list

        out["output_contexts"] = (
            capo_lex_models_v2.types.output_contexts_list.deserialize_json(
                data["outputContexts"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    return out
