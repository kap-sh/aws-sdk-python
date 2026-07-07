"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ElicitationCodeHookInvocationSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.boxed_boolean
    import aws_sdk_lex_models_v2.types.name


class ElicitationCodeHookInvocationSetting(TypedDict, closed=True):
    enable_code_hook_invocation: (
        "aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    )
    """<p>Indicates whether a Lambda function should be invoked for the dialog.</p>"""
    invocation_label: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>A label that indicates the dialog step from which the dialog code hook is happening.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElicitationCodeHookInvocationSetting) -> dict:
    out: dict = {}
    out["enableCodeHookInvocation"] = value["enable_code_hook_invocation"]
    if "invocation_label" in value:
        out["invocationLabel"] = value["invocation_label"]
    return out


def deserialize_json(data: dict) -> ElicitationCodeHookInvocationSetting:
    out: ElicitationCodeHookInvocationSetting = {}  # type: ignore[typeddict-item]
    if "enableCodeHookInvocation" in data:
        out["enable_code_hook_invocation"] = data["enableCodeHookInvocation"]
    else:
        raise DeserializationError(
            "ElicitationCodeHookInvocationSetting.enable_code_hook_invocation required"
        )
    if "invocationLabel" in data:
        out["invocation_label"] = data["invocationLabel"]
    return out
