"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentClosingSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.boxed_boolean
    import aws_sdk_lex_models_v2.types.conditional_specification
    import aws_sdk_lex_models_v2.types.dialog_state
    import aws_sdk_lex_models_v2.types.response_specification


class IntentClosingSetting(TypedDict, closed=True):
    closing_response: NotRequired[
        "aws_sdk_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    """<p>The response that Amazon Lex sends to the user when the intent is complete.</p>"""
    active: NotRequired["aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether an intent's closing response is used. When this field is false, the closing response isn't sent to the user. If the <code>active</code> field isn't specified, the default is true.</p>"""
    next_step: NotRequired["aws_sdk_lex_models_v2.types.dialog_state.DialogState"]
    """<p>Specifies the next step that the bot executes after playing the intent's closing response.</p>"""
    conditional: NotRequired[
        "aws_sdk_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    """<p>A list of conditional branches associated with the intent's closing response. These branches are executed when the <code>nextStep</code> attribute is set to <code>EvalutateConditional</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentClosingSetting) -> dict:
    out: dict = {}
    if "closing_response" in value:
        import aws_sdk_lex_models_v2.types.response_specification

        out["closingResponse"] = (
            aws_sdk_lex_models_v2.types.response_specification.serialize_json(
                value["closing_response"]
            )
        )
    if "active" in value:
        out["active"] = value["active"]
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
    return out


def deserialize_json(data: dict) -> IntentClosingSetting:
    out: IntentClosingSetting = {}  # type: ignore[typeddict-item]
    if "closingResponse" in data:
        import aws_sdk_lex_models_v2.types.response_specification

        out["closing_response"] = (
            aws_sdk_lex_models_v2.types.response_specification.deserialize_json(
                data["closingResponse"]
            )
        )
    if "active" in data:
        out["active"] = data["active"]
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
    return out
