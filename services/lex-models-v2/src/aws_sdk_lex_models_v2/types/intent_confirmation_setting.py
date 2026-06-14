"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentConfirmationSetting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.boxed_boolean
    import aws_sdk_lex_models_v2.types.conditional_specification
    import aws_sdk_lex_models_v2.types.dialog_code_hook_invocation_setting
    import aws_sdk_lex_models_v2.types.dialog_state
    import aws_sdk_lex_models_v2.types.elicitation_code_hook_invocation_setting
    import aws_sdk_lex_models_v2.types.prompt_specification
    import aws_sdk_lex_models_v2.types.response_specification


class IntentConfirmationSetting(TypedDict):
    prompt_specification: (
        "aws_sdk_lex_models_v2.types.prompt_specification.PromptSpecification"
    )
    """<p>Prompts the user to confirm the intent. This question should have a yes or no answer.</p> <p>Amazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for fulfillment. For example, with the <code>OrderPizza</code> intent, you might want to confirm that the order is correct before placing it. For other intents, such as intents that simply respond to user questions, you might not need to ask the user for confirmation before providing the information. </p>"""
    declination_response: NotRequired[
        "aws_sdk_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    r"""<p>When the user answers \"no\" to the question defined in <code>promptSpecification</code>, Amazon Lex responds with this response to acknowledge that the intent was canceled. </p>"""
    active: NotRequired["aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether the intent's confirmation is sent to the user. When this field is false, confirmation and declination responses aren't sent. If the <code>active</code> field isn't specified, the default is true.</p>"""
    confirmation_response: NotRequired[
        "aws_sdk_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    confirmation_next_step: NotRequired[
        "aws_sdk_lex_models_v2.types.dialog_state.DialogState"
    ]
    """<p>Specifies the next step that the bot executes when the customer confirms the intent.</p>"""
    confirmation_conditional: NotRequired[
        "aws_sdk_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    """<p>A list of conditional branches to evaluate after the intent is closed.</p>"""
    declination_next_step: NotRequired[
        "aws_sdk_lex_models_v2.types.dialog_state.DialogState"
    ]
    """<p>Specifies the next step that the bot executes when the customer declines the intent.</p>"""
    declination_conditional: NotRequired[
        "aws_sdk_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    """<p>A list of conditional branches to evaluate after the intent is declined.</p>"""
    failure_response: NotRequired[
        "aws_sdk_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    failure_next_step: NotRequired[
        "aws_sdk_lex_models_v2.types.dialog_state.DialogState"
    ]
    """<p>The next step to take in the conversation if the confirmation step fails.</p>"""
    failure_conditional: NotRequired[
        "aws_sdk_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    code_hook: NotRequired[
        "aws_sdk_lex_models_v2.types.dialog_code_hook_invocation_setting.DialogCodeHookInvocationSetting"
    ]
    """<p>The <code>DialogCodeHookInvocationSetting</code> object associated with intent's confirmation step. The dialog code hook is triggered based on these invocation settings when the confirmation next step or declination next step or failure next step is <code>InvokeDialogCodeHook</code>. </p>"""
    elicitation_code_hook: NotRequired[
        "aws_sdk_lex_models_v2.types.elicitation_code_hook_invocation_setting.ElicitationCodeHookInvocationSetting"
    ]
    """<p>The <code>DialogCodeHookInvocationSetting</code> used when the code hook is invoked during confirmation prompt retries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentConfirmationSetting) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.prompt_specification

    out["promptSpecification"] = (
        aws_sdk_lex_models_v2.types.prompt_specification.serialize_json(
            value["prompt_specification"]
        )
    )
    if "declination_response" in value:
        import aws_sdk_lex_models_v2.types.response_specification

        out["declinationResponse"] = (
            aws_sdk_lex_models_v2.types.response_specification.serialize_json(
                value["declination_response"]
            )
        )
    if "active" in value:
        out["active"] = value["active"]
    if "confirmation_response" in value:
        import aws_sdk_lex_models_v2.types.response_specification

        out["confirmationResponse"] = (
            aws_sdk_lex_models_v2.types.response_specification.serialize_json(
                value["confirmation_response"]
            )
        )
    if "confirmation_next_step" in value:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["confirmationNextStep"] = (
            aws_sdk_lex_models_v2.types.dialog_state.serialize_json(
                value["confirmation_next_step"]
            )
        )
    if "confirmation_conditional" in value:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["confirmationConditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.serialize_json(
                value["confirmation_conditional"]
            )
        )
    if "declination_next_step" in value:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["declinationNextStep"] = (
            aws_sdk_lex_models_v2.types.dialog_state.serialize_json(
                value["declination_next_step"]
            )
        )
    if "declination_conditional" in value:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["declinationConditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.serialize_json(
                value["declination_conditional"]
            )
        )
    if "failure_response" in value:
        import aws_sdk_lex_models_v2.types.response_specification

        out["failureResponse"] = (
            aws_sdk_lex_models_v2.types.response_specification.serialize_json(
                value["failure_response"]
            )
        )
    if "failure_next_step" in value:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["failureNextStep"] = (
            aws_sdk_lex_models_v2.types.dialog_state.serialize_json(
                value["failure_next_step"]
            )
        )
    if "failure_conditional" in value:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["failureConditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.serialize_json(
                value["failure_conditional"]
            )
        )
    if "code_hook" in value:
        import aws_sdk_lex_models_v2.types.dialog_code_hook_invocation_setting

        out["codeHook"] = (
            aws_sdk_lex_models_v2.types.dialog_code_hook_invocation_setting.serialize_json(
                value["code_hook"]
            )
        )
    if "elicitation_code_hook" in value:
        import aws_sdk_lex_models_v2.types.elicitation_code_hook_invocation_setting

        out["elicitationCodeHook"] = (
            aws_sdk_lex_models_v2.types.elicitation_code_hook_invocation_setting.serialize_json(
                value["elicitation_code_hook"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntentConfirmationSetting:
    out: IntentConfirmationSetting = {}  # type: ignore[typeddict-item]
    if "promptSpecification" in data:
        import aws_sdk_lex_models_v2.types.prompt_specification

        out["prompt_specification"] = (
            aws_sdk_lex_models_v2.types.prompt_specification.deserialize_json(
                data["promptSpecification"]
            )
        )
    else:
        raise DeserializationError(
            "IntentConfirmationSetting.prompt_specification required"
        )
    if "declinationResponse" in data:
        import aws_sdk_lex_models_v2.types.response_specification

        out["declination_response"] = (
            aws_sdk_lex_models_v2.types.response_specification.deserialize_json(
                data["declinationResponse"]
            )
        )
    if "active" in data:
        out["active"] = data["active"]
    if "confirmationResponse" in data:
        import aws_sdk_lex_models_v2.types.response_specification

        out["confirmation_response"] = (
            aws_sdk_lex_models_v2.types.response_specification.deserialize_json(
                data["confirmationResponse"]
            )
        )
    if "confirmationNextStep" in data:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["confirmation_next_step"] = (
            aws_sdk_lex_models_v2.types.dialog_state.deserialize_json(
                data["confirmationNextStep"]
            )
        )
    if "confirmationConditional" in data:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["confirmation_conditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.deserialize_json(
                data["confirmationConditional"]
            )
        )
    if "declinationNextStep" in data:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["declination_next_step"] = (
            aws_sdk_lex_models_v2.types.dialog_state.deserialize_json(
                data["declinationNextStep"]
            )
        )
    if "declinationConditional" in data:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["declination_conditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.deserialize_json(
                data["declinationConditional"]
            )
        )
    if "failureResponse" in data:
        import aws_sdk_lex_models_v2.types.response_specification

        out["failure_response"] = (
            aws_sdk_lex_models_v2.types.response_specification.deserialize_json(
                data["failureResponse"]
            )
        )
    if "failureNextStep" in data:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["failure_next_step"] = (
            aws_sdk_lex_models_v2.types.dialog_state.deserialize_json(
                data["failureNextStep"]
            )
        )
    if "failureConditional" in data:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["failure_conditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.deserialize_json(
                data["failureConditional"]
            )
        )
    if "codeHook" in data:
        import aws_sdk_lex_models_v2.types.dialog_code_hook_invocation_setting

        out["code_hook"] = (
            aws_sdk_lex_models_v2.types.dialog_code_hook_invocation_setting.deserialize_json(
                data["codeHook"]
            )
        )
    if "elicitationCodeHook" in data:
        import aws_sdk_lex_models_v2.types.elicitation_code_hook_invocation_setting

        out["elicitation_code_hook"] = (
            aws_sdk_lex_models_v2.types.elicitation_code_hook_invocation_setting.deserialize_json(
                data["elicitationCodeHook"]
            )
        )
    return out
