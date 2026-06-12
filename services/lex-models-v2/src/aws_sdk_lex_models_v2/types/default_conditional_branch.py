"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DefaultConditionalBranch``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.dialog_state
    import aws_sdk_lex_models_v2.types.response_specification


class DefaultConditionalBranch(TypedDict):
    next_step: NotRequired["aws_sdk_lex_models_v2.types.dialog_state.DialogState"]
    """<p>The next step in the conversation.</p>"""
    response: NotRequired[
        "aws_sdk_lex_models_v2.types.response_specification.ResponseSpecification"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DefaultConditionalBranch) -> dict:
    out: dict = {}
    if "next_step" in value:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["nextStep"] = aws_sdk_lex_models_v2.types.dialog_state.serialize_json(
            value["next_step"]
        )
    if "response" in value:
        import aws_sdk_lex_models_v2.types.response_specification

        out["response"] = (
            aws_sdk_lex_models_v2.types.response_specification.serialize_json(
                value["response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultConditionalBranch:
    out: DefaultConditionalBranch = {}  # type: ignore[typeddict-item]
    if "nextStep" in data:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["next_step"] = aws_sdk_lex_models_v2.types.dialog_state.deserialize_json(
            data["nextStep"]
        )
    if "response" in data:
        import aws_sdk_lex_models_v2.types.response_specification

        out["response"] = (
            aws_sdk_lex_models_v2.types.response_specification.deserialize_json(
                data["response"]
            )
        )
    return out
