"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotCaptureSetting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.conditional_specification
    import aws_sdk_lex_models_v2.types.dialog_code_hook_invocation_setting
    import aws_sdk_lex_models_v2.types.dialog_state
    import aws_sdk_lex_models_v2.types.elicitation_code_hook_invocation_setting
    import aws_sdk_lex_models_v2.types.response_specification


class SlotCaptureSetting(TypedDict):
    capture_response: NotRequired[
        "aws_sdk_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    capture_next_step: NotRequired[
        "aws_sdk_lex_models_v2.types.dialog_state.DialogState"
    ]
    """<p>Specifies the next step that the bot runs when the slot value is captured before the code hook times out.</p>"""
    capture_conditional: NotRequired[
        "aws_sdk_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    """<p>A list of conditional branches to evaluate after the slot value is captured.</p>"""
    failure_response: NotRequired[
        "aws_sdk_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    failure_next_step: NotRequired[
        "aws_sdk_lex_models_v2.types.dialog_state.DialogState"
    ]
    """<p>Specifies the next step that the bot runs when the slot value code is not recognized.</p>"""
    failure_conditional: NotRequired[
        "aws_sdk_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    """<p>A list of conditional branches to evaluate when the slot value isn't captured.</p>"""
    code_hook: NotRequired[
        "aws_sdk_lex_models_v2.types.dialog_code_hook_invocation_setting.DialogCodeHookInvocationSetting"
    ]
    """<p>Code hook called after Amazon Lex successfully captures a slot value.</p>"""
    elicitation_code_hook: NotRequired[
        "aws_sdk_lex_models_v2.types.elicitation_code_hook_invocation_setting.ElicitationCodeHookInvocationSetting"
    ]
    """<p>Code hook called when Amazon Lex doesn't capture a slot value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotCaptureSetting) -> dict:
    out: dict = {}
    if "capture_response" in value:
        import aws_sdk_lex_models_v2.types.response_specification

        out["captureResponse"] = (
            aws_sdk_lex_models_v2.types.response_specification.serialize_json(
                value["capture_response"]
            )
        )
    if "capture_next_step" in value:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["captureNextStep"] = (
            aws_sdk_lex_models_v2.types.dialog_state.serialize_json(
                value["capture_next_step"]
            )
        )
    if "capture_conditional" in value:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["captureConditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.serialize_json(
                value["capture_conditional"]
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


def deserialize_json(data: dict) -> SlotCaptureSetting:
    out: SlotCaptureSetting = {}  # type: ignore[typeddict-item]
    if "captureResponse" in data:
        import aws_sdk_lex_models_v2.types.response_specification

        out["capture_response"] = (
            aws_sdk_lex_models_v2.types.response_specification.deserialize_json(
                data["captureResponse"]
            )
        )
    if "captureNextStep" in data:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["capture_next_step"] = (
            aws_sdk_lex_models_v2.types.dialog_state.deserialize_json(
                data["captureNextStep"]
            )
        )
    if "captureConditional" in data:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["capture_conditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.deserialize_json(
                data["captureConditional"]
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
