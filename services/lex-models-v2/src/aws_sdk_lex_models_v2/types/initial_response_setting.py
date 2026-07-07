"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#InitialResponseSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.conditional_specification
    import aws_sdk_lex_models_v2.types.dialog_code_hook_invocation_setting
    import aws_sdk_lex_models_v2.types.dialog_state
    import aws_sdk_lex_models_v2.types.response_specification


class InitialResponseSetting(TypedDict, closed=True):
    initial_response: NotRequired[
        "aws_sdk_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    next_step: NotRequired["aws_sdk_lex_models_v2.types.dialog_state.DialogState"]
    """<p>The next step in the conversation.</p>"""
    conditional: NotRequired[
        "aws_sdk_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    code_hook: NotRequired[
        "aws_sdk_lex_models_v2.types.dialog_code_hook_invocation_setting.DialogCodeHookInvocationSetting"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InitialResponseSetting) -> dict:
    out: dict = {}
    if "initial_response" in value:
        import aws_sdk_lex_models_v2.types.response_specification

        out["initialResponse"] = (
            aws_sdk_lex_models_v2.types.response_specification.serialize_json(
                value["initial_response"]
            )
        )
    if "next_step" in value:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["nextStep"] = aws_sdk_lex_models_v2.types.dialog_state.serialize_json(
            value["next_step"]
        )
    if "conditional" in value:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["conditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.serialize_json(
                value["conditional"]
            )
        )
    if "code_hook" in value:
        import aws_sdk_lex_models_v2.types.dialog_code_hook_invocation_setting

        out["codeHook"] = (
            aws_sdk_lex_models_v2.types.dialog_code_hook_invocation_setting.serialize_json(
                value["code_hook"]
            )
        )
    return out


def deserialize_json(data: dict) -> InitialResponseSetting:
    out: InitialResponseSetting = {}  # type: ignore[typeddict-item]
    if "initialResponse" in data:
        import aws_sdk_lex_models_v2.types.response_specification

        out["initial_response"] = (
            aws_sdk_lex_models_v2.types.response_specification.deserialize_json(
                data["initialResponse"]
            )
        )
    if "nextStep" in data:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["next_step"] = aws_sdk_lex_models_v2.types.dialog_state.deserialize_json(
            data["nextStep"]
        )
    if "conditional" in data:
        import aws_sdk_lex_models_v2.types.conditional_specification

        out["conditional"] = (
            aws_sdk_lex_models_v2.types.conditional_specification.deserialize_json(
                data["conditional"]
            )
        )
    if "codeHook" in data:
        import aws_sdk_lex_models_v2.types.dialog_code_hook_invocation_setting

        out["code_hook"] = (
            aws_sdk_lex_models_v2.types.dialog_code_hook_invocation_setting.deserialize_json(
                data["codeHook"]
            )
        )
    return out
