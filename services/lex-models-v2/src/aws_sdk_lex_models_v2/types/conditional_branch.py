"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConditionalBranch``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.condition
    import aws_sdk_lex_models_v2.types.dialog_state
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.response_specification


class ConditionalBranch(TypedDict):
    name: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The name of the branch. </p>"""
    condition: "aws_sdk_lex_models_v2.types.condition.Condition"
    """<p>Contains the expression to evaluate. If the condition is true, the branch's actions are taken.</p>"""
    next_step: "aws_sdk_lex_models_v2.types.dialog_state.DialogState"
    """<p>The next step in the conversation.</p>"""
    response: NotRequired[
        "aws_sdk_lex_models_v2.types.response_specification.ResponseSpecification"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalBranch) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_lex_models_v2.types.condition

    out["condition"] = aws_sdk_lex_models_v2.types.condition.serialize_json(
        value["condition"]
    )
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


def deserialize_json(data: dict) -> ConditionalBranch:
    out: ConditionalBranch = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConditionalBranch.name required")
    if "condition" in data:
        import aws_sdk_lex_models_v2.types.condition

        out["condition"] = aws_sdk_lex_models_v2.types.condition.deserialize_json(
            data["condition"]
        )
    else:
        raise DeserializationError("ConditionalBranch.condition required")
    if "nextStep" in data:
        import aws_sdk_lex_models_v2.types.dialog_state

        out["next_step"] = aws_sdk_lex_models_v2.types.dialog_state.deserialize_json(
            data["nextStep"]
        )
    else:
        raise DeserializationError("ConditionalBranch.next_step required")
    if "response" in data:
        import aws_sdk_lex_models_v2.types.response_specification

        out["response"] = (
            aws_sdk_lex_models_v2.types.response_specification.deserialize_json(
                data["response"]
            )
        )
    return out
