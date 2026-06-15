"""Generated from Smithy shape ``com.amazonaws.bedrock#SelectiveContentGuarding``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.selective_guarding_mode


class SelectiveContentGuarding(TypedDict):
    system: NotRequired[
        "aws_sdk_bedrock.types.selective_guarding_mode.SelectiveGuardingMode"
    ]
    r"""<p>Selective guarding mode for system prompts.\"</p>"""
    messages: NotRequired[
        "aws_sdk_bedrock.types.selective_guarding_mode.SelectiveGuardingMode"
    ]
    """<p>Selective guarding mode for user messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelectiveContentGuarding) -> dict:
    out: dict = {}
    if "system" in value:
        import aws_sdk_bedrock.types.selective_guarding_mode

        out["system"] = aws_sdk_bedrock.types.selective_guarding_mode.serialize_json(
            value["system"]
        )
    if "messages" in value:
        import aws_sdk_bedrock.types.selective_guarding_mode

        out["messages"] = aws_sdk_bedrock.types.selective_guarding_mode.serialize_json(
            value["messages"]
        )
    return out


def deserialize_json(data: dict) -> SelectiveContentGuarding:
    out: SelectiveContentGuarding = {}  # type: ignore[typeddict-item]
    if "system" in data:
        import aws_sdk_bedrock.types.selective_guarding_mode

        out["system"] = aws_sdk_bedrock.types.selective_guarding_mode.deserialize_json(
            data["system"]
        )
    if "messages" in data:
        import aws_sdk_bedrock.types.selective_guarding_mode

        out["messages"] = (
            aws_sdk_bedrock.types.selective_guarding_mode.deserialize_json(
                data["messages"]
            )
        )
    return out
