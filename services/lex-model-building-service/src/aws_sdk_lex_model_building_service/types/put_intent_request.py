"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#PutIntentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

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


class PutIntentRequest(TypedDict):
    name: "aws_sdk_lex_model_building_service.types.intent_name.IntentName"
    r"""<p>The name of the intent. The name is <i>not</i> case sensitive. </p> <p>The name can't match a built-in intent name, or a built-in intent name with \"AMAZON.\" removed. For example, because there is a built-in intent called <code>AMAZON.HelpIntent</code>, you can't create a custom intent called <code>HelpIntent</code>.</p> <p>For a list of built-in intents, see <a href=\"https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.</p>"""
    description: NotRequired[
        "aws_sdk_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the intent.</p>"""
    slots: NotRequired["aws_sdk_lex_model_building_service.types.slot_list.SlotList"]
    """<p>An array of intent slots. At runtime, Amazon Lex elicits required slot values from the user using prompts defined in the slots. For more information, see <a>how-it-works</a>. </p>"""
    sample_utterances: NotRequired[
        "aws_sdk_lex_model_building_service.types.intent_utterance_list.IntentUtteranceList"
    ]
    r"""<p>An array of utterances (strings) that a user might say to signal the intent. For example, \"I want {PizzaSize} pizza\", \"Order {Quantity} {PizzaSize} pizzas\". </p> <p>In each utterance, a slot name is enclosed in curly braces. </p>"""
    confirmation_prompt: NotRequired[
        "aws_sdk_lex_model_building_service.types.prompt.Prompt"
    ]
    """<p>Prompts the user to confirm the intent. This question should have a yes or no answer.</p> <p>Amazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for fulfillment. For example, with the <code>OrderPizza</code> intent, you might want to confirm that the order is correct before placing it. For other intents, such as intents that simply respond to user questions, you might not need to ask the user for confirmation before providing the information. </p> <note> <p>You you must provide both the <code>rejectionStatement</code> and the <code>confirmationPrompt</code>, or neither.</p> </note>"""
    rejection_statement: NotRequired[
        "aws_sdk_lex_model_building_service.types.statement.Statement"
    ]
    r"""<p>When the user answers \"no\" to the question defined in <code>confirmationPrompt</code>, Amazon Lex responds with this statement to acknowledge that the intent was canceled. </p> <note> <p>You must provide both the <code>rejectionStatement</code> and the <code>confirmationPrompt</code>, or neither.</p> </note>"""
    follow_up_prompt: NotRequired[
        "aws_sdk_lex_model_building_service.types.follow_up_prompt.FollowUpPrompt"
    ]
    r"""<p>Amazon Lex uses this prompt to solicit additional activity after fulfilling an intent. For example, after the <code>OrderPizza</code> intent is fulfilled, you might prompt the user to order a drink.</p> <p>The action that Amazon Lex takes depends on the user's response, as follows:</p> <ul> <li> <p>If the user says \"Yes\" it responds with the clarification prompt that is configured for the bot.</p> </li> <li> <p>if the user says \"Yes\" and continues with an utterance that triggers an intent it starts a conversation for the intent.</p> </li> <li> <p>If the user says \"No\" it responds with the rejection statement configured for the the follow-up prompt.</p> </li> <li> <p>If it doesn't recognize the utterance it repeats the follow-up prompt again.</p> </li> </ul> <p>The <code>followUpPrompt</code> field and the <code>conclusionStatement</code> field are mutually exclusive. You can specify only one. </p>"""
    conclusion_statement: NotRequired[
        "aws_sdk_lex_model_building_service.types.statement.Statement"
    ]
    """<p> The statement that you want Amazon Lex to convey to the user after the intent is successfully fulfilled by the Lambda function. </p> <p>This element is relevant only if you provide a Lambda function in the <code>fulfillmentActivity</code>. If you return the intent to the client application, you can't specify this element.</p> <note> <p>The <code>followUpPrompt</code> and <code>conclusionStatement</code> are mutually exclusive. You can specify only one.</p> </note>"""
    dialog_code_hook: NotRequired[
        "aws_sdk_lex_model_building_service.types.code_hook.CodeHook"
    ]
    """<p> Specifies a Lambda function to invoke for each user input. You can invoke this Lambda function to personalize user interaction. </p> <p>For example, suppose your bot determines that the user is John. Your Lambda function might retrieve John's information from a backend database and prepopulate some of the values. For example, if you find that John is gluten intolerant, you might set the corresponding intent slot, <code>GlutenIntolerant</code>, to true. You might find John's phone number and set the corresponding session attribute. </p>"""
    fulfillment_activity: NotRequired[
        "aws_sdk_lex_model_building_service.types.fulfillment_activity.FulfillmentActivity"
    ]
    """<p>Required. Describes how the intent is fulfilled. For example, after a user provides all of the information for a pizza order, <code>fulfillmentActivity</code> defines how the bot places an order with a local pizza store. </p> <p> You might configure Amazon Lex to return all of the intent information to the client application, or direct it to invoke a Lambda function that can process the intent (for example, place an order with a pizzeria). </p>"""
    parent_intent_signature: NotRequired[
        "aws_sdk_lex_model_building_service.types.builtin_intent_signature.BuiltinIntentSignature"
    ]
    r"""<p>A unique identifier for the built-in intent to base this intent on. To find the signature for an intent, see <a href=\"https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.</p>"""
    checksum: NotRequired["aws_sdk_lex_model_building_service.types.string.String"]
    """<p>Identifies a specific revision of the <code>$LATEST</code> version.</p> <p>When you create a new intent, leave the <code>checksum</code> field blank. If you specify a checksum you get a <code>BadRequestException</code> exception.</p> <p>When you want to update a intent, set the <code>checksum</code> field to the checksum of the most recent revision of the <code>$LATEST</code> version. If you don't specify the <code> checksum</code> field, or if the checksum does not match the <code>$LATEST</code> version, you get a <code>PreconditionFailedException</code> exception.</p>"""
    create_version: NotRequired[
        "aws_sdk_lex_model_building_service.types.boolean.Boolean"
    ]
    """<p>When set to <code>true</code> a new numbered version of the intent is created. This is the same as calling the <code>CreateIntentVersion</code> operation. If you do not specify <code>createVersion</code>, the default is <code>false</code>.</p>"""
    kendra_configuration: NotRequired[
        "aws_sdk_lex_model_building_service.types.kendra_configuration.KendraConfiguration"
    ]
    r"""<p>Configuration information required to use the <code>AMAZON.KendraSearchIntent</code> intent to connect to an Amazon Kendra index. For more information, see <a href=\"http://docs.aws.amazon.com/lex/latest/dg/built-in-intent-kendra-search.html\"> AMAZON.KendraSearchIntent</a>.</p>"""
    input_contexts: NotRequired[
        "aws_sdk_lex_model_building_service.types.input_context_list.InputContextList"
    ]
    """<p>An array of <code>InputContext</code> objects that lists the contexts that must be active for Amazon Lex to choose the intent in a conversation with the user.</p>"""
    output_contexts: NotRequired[
        "aws_sdk_lex_model_building_service.types.output_context_list.OutputContextList"
    ]
    """<p>An array of <code>OutputContext</code> objects that lists the contexts that the intent activates when the intent is fulfilled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutIntentRequest) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> PutIntentRequest:
    out: PutIntentRequest = {}  # type: ignore[typeddict-item]
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
