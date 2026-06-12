"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateIntentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.dialog_code_hook_settings
    import aws_sdk_lex_models_v2.types.display_name
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.fulfillment_code_hook_settings
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.initial_response_setting
    import aws_sdk_lex_models_v2.types.input_contexts_list
    import aws_sdk_lex_models_v2.types.intent_closing_setting
    import aws_sdk_lex_models_v2.types.intent_confirmation_setting
    import aws_sdk_lex_models_v2.types.intent_signature
    import aws_sdk_lex_models_v2.types.kendra_configuration
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.output_contexts_list
    import aws_sdk_lex_models_v2.types.q_in_connect_intent_configuration
    import aws_sdk_lex_models_v2.types.qn_a_intent_configuration
    import aws_sdk_lex_models_v2.types.sample_utterances_list
    import aws_sdk_lex_models_v2.types.slot_priorities_list
    import aws_sdk_lex_models_v2.types.timestamp


class UpdateIntentResponse(TypedDict):
    intent_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the intent that was updated.</p>"""
    intent_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The updated name of the intent.</p>"""
    intent_display_name: NotRequired[
        "aws_sdk_lex_models_v2.types.display_name.DisplayName"
    ]
    """<p>The updated display name of the intent.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The updated description of the intent.</p>"""
    parent_intent_signature: NotRequired[
        "aws_sdk_lex_models_v2.types.intent_signature.IntentSignature"
    ]
    """<p>The updated built-in intent that is the parent of this intent.</p>"""
    sample_utterances: NotRequired[
        "aws_sdk_lex_models_v2.types.sample_utterances_list.SampleUtterancesList"
    ]
    """<p>The updated list of sample utterances for the intent.</p>"""
    dialog_code_hook: NotRequired[
        "aws_sdk_lex_models_v2.types.dialog_code_hook_settings.DialogCodeHookSettings"
    ]
    """<p>The updated Lambda function called during each turn of the conversation with the user.</p>"""
    fulfillment_code_hook: NotRequired[
        "aws_sdk_lex_models_v2.types.fulfillment_code_hook_settings.FulfillmentCodeHookSettings"
    ]
    """<p>The updated Lambda function called when the intent is ready for fulfillment.</p>"""
    slot_priorities: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_priorities_list.SlotPrioritiesList"
    ]
    """<p>The updated list of slots and their priorities that are elicited from the user for the intent.</p>"""
    intent_confirmation_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.intent_confirmation_setting.IntentConfirmationSetting"
    ]
    """<p>The updated prompts that Amazon Lex sends to the user to confirm the completion of an intent.</p>"""
    intent_closing_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.intent_closing_setting.IntentClosingSetting"
    ]
    """<p>The updated response that Amazon Lex sends the user when the intent is closed.</p>"""
    input_contexts: NotRequired[
        "aws_sdk_lex_models_v2.types.input_contexts_list.InputContextsList"
    ]
    """<p>The updated list of contexts that must be active for the intent to be considered by Amazon Lex.</p>"""
    output_contexts: NotRequired[
        "aws_sdk_lex_models_v2.types.output_contexts_list.OutputContextsList"
    ]
    """<p>The updated list of contexts that Amazon Lex activates when the intent is fulfilled.</p>"""
    kendra_configuration: NotRequired[
        "aws_sdk_lex_models_v2.types.kendra_configuration.KendraConfiguration"
    ]
    """<p>The updated configuration for connecting to an Amazon Kendra index with the <code>AMAZON.KendraSearchIntent</code> intent.</p>"""
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot that contains the intent.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot that contains the intent. Will always be <code>DRAFT</code>.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The updated language and locale of the intent.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of when the intent was created.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>A timestamp of the last time that the intent was modified.</p>"""
    initial_response_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.initial_response_setting.InitialResponseSetting"
    ]
    """<p>Configuration settings for a response sent to the user before Amazon Lex starts eliciting slots.</p>"""
    qn_a_intent_configuration: NotRequired[
        "aws_sdk_lex_models_v2.types.qn_a_intent_configuration.QnAIntentConfiguration"
    ]
    """<p>Details about the configuration of the built-in <code>Amazon.QnAIntent</code>.</p>"""
    q_in_connect_intent_configuration: NotRequired[
        "aws_sdk_lex_models_v2.types.q_in_connect_intent_configuration.QInConnectIntentConfiguration"
    ]
    """<p>Qinconnect intent configuration details for the update intent response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntentResponse) -> dict:
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
    if "sample_utterances" in value:
        import aws_sdk_lex_models_v2.types.sample_utterances_list

        out["sampleUtterances"] = (
            aws_sdk_lex_models_v2.types.sample_utterances_list.serialize_json(
                value["sample_utterances"]
            )
        )
    if "dialog_code_hook" in value:
        import aws_sdk_lex_models_v2.types.dialog_code_hook_settings

        out["dialogCodeHook"] = (
            aws_sdk_lex_models_v2.types.dialog_code_hook_settings.serialize_json(
                value["dialog_code_hook"]
            )
        )
    if "fulfillment_code_hook" in value:
        import aws_sdk_lex_models_v2.types.fulfillment_code_hook_settings

        out["fulfillmentCodeHook"] = (
            aws_sdk_lex_models_v2.types.fulfillment_code_hook_settings.serialize_json(
                value["fulfillment_code_hook"]
            )
        )
    if "slot_priorities" in value:
        import aws_sdk_lex_models_v2.types.slot_priorities_list

        out["slotPriorities"] = (
            aws_sdk_lex_models_v2.types.slot_priorities_list.serialize_json(
                value["slot_priorities"]
            )
        )
    if "intent_confirmation_setting" in value:
        import aws_sdk_lex_models_v2.types.intent_confirmation_setting

        out["intentConfirmationSetting"] = (
            aws_sdk_lex_models_v2.types.intent_confirmation_setting.serialize_json(
                value["intent_confirmation_setting"]
            )
        )
    if "intent_closing_setting" in value:
        import aws_sdk_lex_models_v2.types.intent_closing_setting

        out["intentClosingSetting"] = (
            aws_sdk_lex_models_v2.types.intent_closing_setting.serialize_json(
                value["intent_closing_setting"]
            )
        )
    if "input_contexts" in value:
        import aws_sdk_lex_models_v2.types.input_contexts_list

        out["inputContexts"] = (
            aws_sdk_lex_models_v2.types.input_contexts_list.serialize_json(
                value["input_contexts"]
            )
        )
    if "output_contexts" in value:
        import aws_sdk_lex_models_v2.types.output_contexts_list

        out["outputContexts"] = (
            aws_sdk_lex_models_v2.types.output_contexts_list.serialize_json(
                value["output_contexts"]
            )
        )
    if "kendra_configuration" in value:
        import aws_sdk_lex_models_v2.types.kendra_configuration

        out["kendraConfiguration"] = (
            aws_sdk_lex_models_v2.types.kendra_configuration.serialize_json(
                value["kendra_configuration"]
            )
        )
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["last_updated_date_time"]
            )
        )
    if "initial_response_setting" in value:
        import aws_sdk_lex_models_v2.types.initial_response_setting

        out["initialResponseSetting"] = (
            aws_sdk_lex_models_v2.types.initial_response_setting.serialize_json(
                value["initial_response_setting"]
            )
        )
    if "qn_a_intent_configuration" in value:
        import aws_sdk_lex_models_v2.types.qn_a_intent_configuration

        out["qnAIntentConfiguration"] = (
            aws_sdk_lex_models_v2.types.qn_a_intent_configuration.serialize_json(
                value["qn_a_intent_configuration"]
            )
        )
    if "q_in_connect_intent_configuration" in value:
        import aws_sdk_lex_models_v2.types.q_in_connect_intent_configuration

        out["qInConnectIntentConfiguration"] = (
            aws_sdk_lex_models_v2.types.q_in_connect_intent_configuration.serialize_json(
                value["q_in_connect_intent_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateIntentResponse:
    out: UpdateIntentResponse = {}  # type: ignore[typeddict-item]
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
    if "sampleUtterances" in data:
        import aws_sdk_lex_models_v2.types.sample_utterances_list

        out["sample_utterances"] = (
            aws_sdk_lex_models_v2.types.sample_utterances_list.deserialize_json(
                data["sampleUtterances"]
            )
        )
    if "dialogCodeHook" in data:
        import aws_sdk_lex_models_v2.types.dialog_code_hook_settings

        out["dialog_code_hook"] = (
            aws_sdk_lex_models_v2.types.dialog_code_hook_settings.deserialize_json(
                data["dialogCodeHook"]
            )
        )
    if "fulfillmentCodeHook" in data:
        import aws_sdk_lex_models_v2.types.fulfillment_code_hook_settings

        out["fulfillment_code_hook"] = (
            aws_sdk_lex_models_v2.types.fulfillment_code_hook_settings.deserialize_json(
                data["fulfillmentCodeHook"]
            )
        )
    if "slotPriorities" in data:
        import aws_sdk_lex_models_v2.types.slot_priorities_list

        out["slot_priorities"] = (
            aws_sdk_lex_models_v2.types.slot_priorities_list.deserialize_json(
                data["slotPriorities"]
            )
        )
    if "intentConfirmationSetting" in data:
        import aws_sdk_lex_models_v2.types.intent_confirmation_setting

        out["intent_confirmation_setting"] = (
            aws_sdk_lex_models_v2.types.intent_confirmation_setting.deserialize_json(
                data["intentConfirmationSetting"]
            )
        )
    if "intentClosingSetting" in data:
        import aws_sdk_lex_models_v2.types.intent_closing_setting

        out["intent_closing_setting"] = (
            aws_sdk_lex_models_v2.types.intent_closing_setting.deserialize_json(
                data["intentClosingSetting"]
            )
        )
    if "inputContexts" in data:
        import aws_sdk_lex_models_v2.types.input_contexts_list

        out["input_contexts"] = (
            aws_sdk_lex_models_v2.types.input_contexts_list.deserialize_json(
                data["inputContexts"]
            )
        )
    if "outputContexts" in data:
        import aws_sdk_lex_models_v2.types.output_contexts_list

        out["output_contexts"] = (
            aws_sdk_lex_models_v2.types.output_contexts_list.deserialize_json(
                data["outputContexts"]
            )
        )
    if "kendraConfiguration" in data:
        import aws_sdk_lex_models_v2.types.kendra_configuration

        out["kendra_configuration"] = (
            aws_sdk_lex_models_v2.types.kendra_configuration.deserialize_json(
                data["kendraConfiguration"]
            )
        )
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    if "initialResponseSetting" in data:
        import aws_sdk_lex_models_v2.types.initial_response_setting

        out["initial_response_setting"] = (
            aws_sdk_lex_models_v2.types.initial_response_setting.deserialize_json(
                data["initialResponseSetting"]
            )
        )
    if "qnAIntentConfiguration" in data:
        import aws_sdk_lex_models_v2.types.qn_a_intent_configuration

        out["qn_a_intent_configuration"] = (
            aws_sdk_lex_models_v2.types.qn_a_intent_configuration.deserialize_json(
                data["qnAIntentConfiguration"]
            )
        )
    if "qInConnectIntentConfiguration" in data:
        import aws_sdk_lex_models_v2.types.q_in_connect_intent_configuration

        out["q_in_connect_intent_configuration"] = (
            aws_sdk_lex_models_v2.types.q_in_connect_intent_configuration.deserialize_json(
                data["qInConnectIntentConfiguration"]
            )
        )
    return out
