"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UserTurnSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.user_turn_input_specification
    import aws_sdk_lex_models_v2.types.user_turn_output_specification


class UserTurnSpecification(TypedDict, closed=True):
    input: "aws_sdk_lex_models_v2.types.user_turn_input_specification.UserTurnInputSpecification"
    """<p>Contains information about the user messages in the turn in the input.</p>"""
    expected: "aws_sdk_lex_models_v2.types.user_turn_output_specification.UserTurnOutputSpecification"
    """<p>Contains results about the expected output for the user turn.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserTurnSpecification) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.user_turn_input_specification

    out["input"] = (
        aws_sdk_lex_models_v2.types.user_turn_input_specification.serialize_json(
            value["input"]
        )
    )
    import aws_sdk_lex_models_v2.types.user_turn_output_specification

    out["expected"] = (
        aws_sdk_lex_models_v2.types.user_turn_output_specification.serialize_json(
            value["expected"]
        )
    )
    return out


def deserialize_json(data: dict) -> UserTurnSpecification:
    out: UserTurnSpecification = {}  # type: ignore[typeddict-item]
    if "input" in data:
        import aws_sdk_lex_models_v2.types.user_turn_input_specification

        out["input"] = (
            aws_sdk_lex_models_v2.types.user_turn_input_specification.deserialize_json(
                data["input"]
            )
        )
    else:
        raise DeserializationError("UserTurnSpecification.input required")
    if "expected" in data:
        import aws_sdk_lex_models_v2.types.user_turn_output_specification

        out["expected"] = (
            aws_sdk_lex_models_v2.types.user_turn_output_specification.deserialize_json(
                data["expected"]
            )
        )
    else:
        raise DeserializationError("UserTurnSpecification.expected required")
    return out
