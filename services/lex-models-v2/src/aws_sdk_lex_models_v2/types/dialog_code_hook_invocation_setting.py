"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DialogCodeHookInvocationSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.boxed_boolean
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.post_dialog_code_hook_invocation_specification


class DialogCodeHookInvocationSetting(TypedDict, closed=True):
    enable_code_hook_invocation: (
        "aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    )
    """<p>Indicates whether a Lambda function should be invoked for the dialog.</p>"""
    active: "aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    """<p>Determines whether a dialog code hook is used when the intent is activated.</p>"""
    invocation_label: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>A label that indicates the dialog step from which the dialog code hook is happening.</p>"""
    post_code_hook_specification: "aws_sdk_lex_models_v2.types.post_dialog_code_hook_invocation_specification.PostDialogCodeHookInvocationSpecification"
    """<p>Contains the responses and actions that Amazon Lex takes after the Lambda function is complete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DialogCodeHookInvocationSetting) -> dict:
    out: dict = {}
    out["enableCodeHookInvocation"] = value["enable_code_hook_invocation"]
    out["active"] = value["active"]
    if "invocation_label" in value:
        out["invocationLabel"] = value["invocation_label"]
    import aws_sdk_lex_models_v2.types.post_dialog_code_hook_invocation_specification

    out["postCodeHookSpecification"] = (
        aws_sdk_lex_models_v2.types.post_dialog_code_hook_invocation_specification.serialize_json(
            value["post_code_hook_specification"]
        )
    )
    return out


def deserialize_json(data: dict) -> DialogCodeHookInvocationSetting:
    out: DialogCodeHookInvocationSetting = {}  # type: ignore[typeddict-item]
    if "enableCodeHookInvocation" in data:
        out["enable_code_hook_invocation"] = data["enableCodeHookInvocation"]
    else:
        raise DeserializationError(
            "DialogCodeHookInvocationSetting.enable_code_hook_invocation required"
        )
    if "active" in data:
        out["active"] = data["active"]
    else:
        raise DeserializationError("DialogCodeHookInvocationSetting.active required")
    if "invocationLabel" in data:
        out["invocation_label"] = data["invocationLabel"]
    if "postCodeHookSpecification" in data:
        import aws_sdk_lex_models_v2.types.post_dialog_code_hook_invocation_specification

        out["post_code_hook_specification"] = (
            aws_sdk_lex_models_v2.types.post_dialog_code_hook_invocation_specification.deserialize_json(
                data["postCodeHookSpecification"]
            )
        )
    else:
        raise DeserializationError(
            "DialogCodeHookInvocationSetting.post_code_hook_specification required"
        )
    return out
