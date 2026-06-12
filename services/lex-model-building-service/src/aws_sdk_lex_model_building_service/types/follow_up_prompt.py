"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#FollowUpPrompt``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.prompt
    import aws_sdk_lex_model_building_service.types.statement


class FollowUpPrompt(TypedDict):
    prompt: "aws_sdk_lex_model_building_service.types.prompt.Prompt"
    """<p>Prompts for information from the user. </p>"""
    rejection_statement: "aws_sdk_lex_model_building_service.types.statement.Statement"
    """<p>If the user answers \"no\" to the question defined in the <code>prompt</code> field, Amazon Lex responds with this statement to acknowledge that the intent was canceled. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FollowUpPrompt) -> dict:
    out: dict = {}
    import aws_sdk_lex_model_building_service.types.prompt

    out["prompt"] = aws_sdk_lex_model_building_service.types.prompt.serialize_json(
        value["prompt"]
    )
    import aws_sdk_lex_model_building_service.types.statement

    out["rejectionStatement"] = (
        aws_sdk_lex_model_building_service.types.statement.serialize_json(
            value["rejection_statement"]
        )
    )
    return out


def deserialize_json(data: dict) -> FollowUpPrompt:
    out: FollowUpPrompt = {}  # type: ignore[typeddict-item]
    if "prompt" in data:
        import aws_sdk_lex_model_building_service.types.prompt

        out["prompt"] = (
            aws_sdk_lex_model_building_service.types.prompt.deserialize_json(
                data["prompt"]
            )
        )
    else:
        raise DeserializationError("FollowUpPrompt.prompt required")
    if "rejectionStatement" in data:
        import aws_sdk_lex_model_building_service.types.statement

        out["rejection_statement"] = (
            aws_sdk_lex_model_building_service.types.statement.deserialize_json(
                data["rejectionStatement"]
            )
        )
    else:
        raise DeserializationError("FollowUpPrompt.rejection_statement required")
    return out
