"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#PutIntentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.boolean
    import aws_sdk_lex_model_building_service.types.builtin_intent_signature
    import aws_sdk_lex_model_building_service.types.code_hook
    import aws_sdk_lex_model_building_service.types.description
    import aws_sdk_lex_model_building_service.types.follow_up_prompt
    import aws_sdk_lex_model_building_service.types.fulfillment_activity
    import aws_sdk_lex_model_building_service.types.input_context_list
    import aws_sdk_lex_model_building_service.types.intent_name
    import aws_sdk_lex_model_building_service.types.intent_utterance_list
    import aws_sdk_lex_model_building_service.types.kendra_configuration
    import aws_sdk_lex_model_building_service.types.output_context_list
    import aws_sdk_lex_model_building_service.types.prompt
    import aws_sdk_lex_model_building_service.types.slot_list
    import aws_sdk_lex_model_building_service.types.statement
    import aws_sdk_lex_model_building_service.types.string
    import aws_sdk_lex_model_building_service.types.timestamp
    import aws_sdk_lex_model_building_service.types.version


class PutIntentResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_lex_model_building_service.types.intent_name.IntentName"]
    """<p>The name of the intent.</p>"""
    description: NotRequired[
        "aws_sdk_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the intent.</p>"""
    slots: NotRequired["aws_sdk_lex_model_building_service.types.slot_list.SlotList"]
    """<p>An array of intent slots that are configured for the intent.</p>"""
    sample_utterances: NotRequired[
        "aws_sdk_lex_model_building_service.types.intent_utterance_list.IntentUtteranceList"
    ]
    """<p> An array of sample utterances that are configured for the intent. </p>"""
    confirmation_prompt: NotRequired[
        "aws_sdk_lex_model_building_service.types.prompt.Prompt"
    ]
    """<p>If defined in the intent, Amazon Lex prompts the user to confirm the intent before fulfilling it.</p>"""
    rejection_statement: NotRequired[
        "aws_sdk_lex_model_building_service.types.statement.Statement"
    ]
    r"""<p>If the user answers \"no\" to the question defined in <code>confirmationPrompt</code> Amazon Lex responds with this statement to acknowledge that the intent was canceled. </p>"""
    follow_up_prompt: NotRequired[
        "aws_sdk_lex_model_building_service.types.follow_up_prompt.FollowUpPrompt"
    ]
    """<p>If defined in the intent, Amazon Lex uses this prompt to solicit additional user activity after the intent is fulfilled.</p>"""
    conclusion_statement: NotRequired[
        "aws_sdk_lex_model_building_service.types.statement.Statement"
    ]
    """<p>After the Lambda function specified in the<code>fulfillmentActivity</code>intent fulfills the intent, Amazon Lex conveys this statement to the user.</p>"""
    dialog_code_hook: NotRequired[
        "aws_sdk_lex_model_building_service.types.code_hook.CodeHook"
    ]
    """<p>If defined in the intent, Amazon Lex invokes this Lambda function for each user input.</p>"""
    fulfillment_activity: NotRequired[
        "aws_sdk_lex_model_building_service.types.fulfillment_activity.FulfillmentActivity"
    ]
    """<p>If defined in the intent, Amazon Lex invokes this Lambda function to fulfill the intent after the user provides all of the information required by the intent.</p>"""
    parent_intent_signature: NotRequired[
        "aws_sdk_lex_model_building_service.types.builtin_intent_signature.BuiltinIntentSignature"
    ]
    """<p>A unique identifier for the built-in intent that this intent is based on.</p>"""
    last_updated_date: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the intent was updated. When you create a resource, the creation date and last update dates are the same.</p>"""
    created_date: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the intent was created.</p>"""
    version: NotRequired["aws_sdk_lex_model_building_service.types.version.Version"]
    """<p>The version of the intent. For a new intent, the version is always <code>$LATEST</code>.</p>"""
    checksum: NotRequired["aws_sdk_lex_model_building_service.types.string.String"]
    """<p>Checksum of the <code>$LATEST</code>version of the intent created or updated.</p>"""
    create_version: NotRequired[
        "aws_sdk_lex_model_building_service.types.boolean.Boolean"
    ]
    """<p> <code>True</code> if a new version of the intent was created. If the <code>createVersion</code> field was not specified in the request, the <code>createVersion</code> field is set to false in the response.</p>"""
    kendra_configuration: NotRequired[
        "aws_sdk_lex_model_building_service.types.kendra_configuration.KendraConfiguration"
    ]
    """<p>Configuration information, if any, required to connect to an Amazon Kendra index and use the <code>AMAZON.KendraSearchIntent</code> intent.</p>"""
    input_contexts: NotRequired[
        "aws_sdk_lex_model_building_service.types.input_context_list.InputContextList"
    ]
    """<p>An array of <code>InputContext</code> objects that lists the contexts that must be active for Amazon Lex to choose the intent in a conversation with the user.</p>"""
    output_contexts: NotRequired[
        "aws_sdk_lex_model_building_service.types.output_context_list.OutputContextList"
    ]
    """<p>An array of <code>OutputContext</code> objects that lists the contexts that the intent activates when the intent is fulfilled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutIntentResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "slots" in value:
        import aws_sdk_lex_model_building_service.types.slot_list

        out["slots"] = (
            aws_sdk_lex_model_building_service.types.slot_list.serialize_json(
                value["slots"]
            )
        )
    if "sample_utterances" in value:
        import aws_sdk_lex_model_building_service.types.intent_utterance_list

        out["sampleUtterances"] = (
            aws_sdk_lex_model_building_service.types.intent_utterance_list.serialize_json(
                value["sample_utterances"]
            )
        )
    if "confirmation_prompt" in value:
        import aws_sdk_lex_model_building_service.types.prompt

        out["confirmationPrompt"] = (
            aws_sdk_lex_model_building_service.types.prompt.serialize_json(
                value["confirmation_prompt"]
            )
        )
    if "rejection_statement" in value:
        import aws_sdk_lex_model_building_service.types.statement

        out["rejectionStatement"] = (
            aws_sdk_lex_model_building_service.types.statement.serialize_json(
                value["rejection_statement"]
            )
        )
    if "follow_up_prompt" in value:
        import aws_sdk_lex_model_building_service.types.follow_up_prompt

        out["followUpPrompt"] = (
            aws_sdk_lex_model_building_service.types.follow_up_prompt.serialize_json(
                value["follow_up_prompt"]
            )
        )
    if "conclusion_statement" in value:
        import aws_sdk_lex_model_building_service.types.statement

        out["conclusionStatement"] = (
            aws_sdk_lex_model_building_service.types.statement.serialize_json(
                value["conclusion_statement"]
            )
        )
    if "dialog_code_hook" in value:
        import aws_sdk_lex_model_building_service.types.code_hook

        out["dialogCodeHook"] = (
            aws_sdk_lex_model_building_service.types.code_hook.serialize_json(
                value["dialog_code_hook"]
            )
        )
    if "fulfillment_activity" in value:
        import aws_sdk_lex_model_building_service.types.fulfillment_activity

        out["fulfillmentActivity"] = (
            aws_sdk_lex_model_building_service.types.fulfillment_activity.serialize_json(
                value["fulfillment_activity"]
            )
        )
    if "parent_intent_signature" in value:
        out["parentIntentSignature"] = value["parent_intent_signature"]
    if "last_updated_date" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["lastUpdatedDate"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["last_updated_date"]
            )
        )
    if "created_date" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["createdDate"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["created_date"]
            )
        )
    if "version" in value:
        out["version"] = value["version"]
    if "checksum" in value:
        out["checksum"] = value["checksum"]
    if "create_version" in value:
        out["createVersion"] = value["create_version"]
    if "kendra_configuration" in value:
        import aws_sdk_lex_model_building_service.types.kendra_configuration

        out["kendraConfiguration"] = (
            aws_sdk_lex_model_building_service.types.kendra_configuration.serialize_json(
                value["kendra_configuration"]
            )
        )
    if "input_contexts" in value:
        import aws_sdk_lex_model_building_service.types.input_context_list

        out["inputContexts"] = (
            aws_sdk_lex_model_building_service.types.input_context_list.serialize_json(
                value["input_contexts"]
            )
        )
    if "output_contexts" in value:
        import aws_sdk_lex_model_building_service.types.output_context_list

        out["outputContexts"] = (
            aws_sdk_lex_model_building_service.types.output_context_list.serialize_json(
                value["output_contexts"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutIntentResponse:
    out: PutIntentResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "slots" in data:
        import aws_sdk_lex_model_building_service.types.slot_list

        out["slots"] = (
            aws_sdk_lex_model_building_service.types.slot_list.deserialize_json(
                data["slots"]
            )
        )
    if "sampleUtterances" in data:
        import aws_sdk_lex_model_building_service.types.intent_utterance_list

        out["sample_utterances"] = (
            aws_sdk_lex_model_building_service.types.intent_utterance_list.deserialize_json(
                data["sampleUtterances"]
            )
        )
    if "confirmationPrompt" in data:
        import aws_sdk_lex_model_building_service.types.prompt

        out["confirmation_prompt"] = (
            aws_sdk_lex_model_building_service.types.prompt.deserialize_json(
                data["confirmationPrompt"]
            )
        )
    if "rejectionStatement" in data:
        import aws_sdk_lex_model_building_service.types.statement

        out["rejection_statement"] = (
            aws_sdk_lex_model_building_service.types.statement.deserialize_json(
                data["rejectionStatement"]
            )
        )
    if "followUpPrompt" in data:
        import aws_sdk_lex_model_building_service.types.follow_up_prompt

        out["follow_up_prompt"] = (
            aws_sdk_lex_model_building_service.types.follow_up_prompt.deserialize_json(
                data["followUpPrompt"]
            )
        )
    if "conclusionStatement" in data:
        import aws_sdk_lex_model_building_service.types.statement

        out["conclusion_statement"] = (
            aws_sdk_lex_model_building_service.types.statement.deserialize_json(
                data["conclusionStatement"]
            )
        )
    if "dialogCodeHook" in data:
        import aws_sdk_lex_model_building_service.types.code_hook

        out["dialog_code_hook"] = (
            aws_sdk_lex_model_building_service.types.code_hook.deserialize_json(
                data["dialogCodeHook"]
            )
        )
    if "fulfillmentActivity" in data:
        import aws_sdk_lex_model_building_service.types.fulfillment_activity

        out["fulfillment_activity"] = (
            aws_sdk_lex_model_building_service.types.fulfillment_activity.deserialize_json(
                data["fulfillmentActivity"]
            )
        )
    if "parentIntentSignature" in data:
        out["parent_intent_signature"] = data["parentIntentSignature"]
    if "lastUpdatedDate" in data:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["last_updated_date"] = (
            aws_sdk_lex_model_building_service.types.timestamp.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if "createdDate" in data:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["created_date"] = (
            aws_sdk_lex_model_building_service.types.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if "version" in data:
        out["version"] = data["version"]
    if "checksum" in data:
        out["checksum"] = data["checksum"]
    if "createVersion" in data:
        out["create_version"] = data["createVersion"]
    if "kendraConfiguration" in data:
        import aws_sdk_lex_model_building_service.types.kendra_configuration

        out["kendra_configuration"] = (
            aws_sdk_lex_model_building_service.types.kendra_configuration.deserialize_json(
                data["kendraConfiguration"]
            )
        )
    if "inputContexts" in data:
        import aws_sdk_lex_model_building_service.types.input_context_list

        out["input_contexts"] = (
            aws_sdk_lex_model_building_service.types.input_context_list.deserialize_json(
                data["inputContexts"]
            )
        )
    if "outputContexts" in data:
        import aws_sdk_lex_model_building_service.types.output_context_list

        out["output_contexts"] = (
            aws_sdk_lex_model_building_service.types.output_context_list.deserialize_json(
                data["outputContexts"]
            )
        )
    return out
