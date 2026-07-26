"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#InitialResponseSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.conditional_specification
    import capo_lex_models_v2.types.dialog_code_hook_invocation_setting
    import capo_lex_models_v2.types.dialog_state
    import capo_lex_models_v2.types.response_specification


class InitialResponseSetting(TypedDict, closed=True):
    initial_response: NotRequired[
        "capo_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    next_step: NotRequired["capo_lex_models_v2.types.dialog_state.DialogState"]
    """<p>The next step in the conversation.</p>"""
    conditional: NotRequired[
        "capo_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    code_hook: NotRequired[
        "capo_lex_models_v2.types.dialog_code_hook_invocation_setting.DialogCodeHookInvocationSetting"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InitialResponseSetting) -> dict:
    out: dict = {}
    if "initial_response" in value:
        import capo_lex_models_v2.types.response_specification

        out["initialResponse"] = (
            capo_lex_models_v2.types.response_specification.serialize_json(
                value["initial_response"]
            )
        )
    if "next_step" in value:
        import capo_lex_models_v2.types.dialog_state

        out["nextStep"] = capo_lex_models_v2.types.dialog_state.serialize_json(
            value["next_step"]
        )
    if "conditional" in value:
        import capo_lex_models_v2.types.conditional_specification

        out["conditional"] = (
            capo_lex_models_v2.types.conditional_specification.serialize_json(
                value["conditional"]
            )
        )
    if "code_hook" in value:
        import capo_lex_models_v2.types.dialog_code_hook_invocation_setting

        out["codeHook"] = (
            capo_lex_models_v2.types.dialog_code_hook_invocation_setting.serialize_json(
                value["code_hook"]
            )
        )
    return out


def deserialize_json(data: dict) -> InitialResponseSetting:
    out: InitialResponseSetting = {}  # type: ignore[typeddict-item]
    if "initialResponse" in data:
        import capo_lex_models_v2.types.response_specification

        out["initial_response"] = (
            capo_lex_models_v2.types.response_specification.deserialize_json(
                data["initialResponse"]
            )
        )
    if "nextStep" in data:
        import capo_lex_models_v2.types.dialog_state

        out["next_step"] = capo_lex_models_v2.types.dialog_state.deserialize_json(
            data["nextStep"]
        )
    if "conditional" in data:
        import capo_lex_models_v2.types.conditional_specification

        out["conditional"] = (
            capo_lex_models_v2.types.conditional_specification.deserialize_json(
                data["conditional"]
            )
        )
    if "codeHook" in data:
        import capo_lex_models_v2.types.dialog_code_hook_invocation_setting

        out["code_hook"] = (
            capo_lex_models_v2.types.dialog_code_hook_invocation_setting.deserialize_json(
                data["codeHook"]
            )
        )
    return out
