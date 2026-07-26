"""Generated from Smithy shape ``com.amazonaws.connect#PromptList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.prompt

PromptList: TypeAlias = list["capo_connect.types.prompt.Prompt"]


# --- restJson1 ser/de ---
def serialize_json(value: PromptList) -> list:
    import capo_connect.types.prompt

    out: list = []
    for item in value:
        out.append(capo_connect.types.prompt.serialize_json(item))
    return out


def deserialize_json(data: list) -> PromptList:
    import capo_connect.types.prompt

    out: PromptList = []
    for item in data:
        out.append(capo_connect.types.prompt.deserialize_json(item))
    return out
