"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ActionGroupSignature``."""

from typing import Literal, TypeAlias, cast

ActionGroupSignature: TypeAlias = Literal[
    "AMAZON.UserInput",
    "AMAZON.CodeInterpreter",
    "ANTHROPIC.Computer",
    "ANTHROPIC.Bash",
    "ANTHROPIC.TextEditor",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionGroupSignature) -> str:
    return value


def deserialize_json(data: str) -> ActionGroupSignature:
    return cast(ActionGroupSignature, data)
