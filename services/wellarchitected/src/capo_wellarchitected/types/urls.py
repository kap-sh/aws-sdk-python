"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Urls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.choice_content

Urls: TypeAlias = list["capo_wellarchitected.types.choice_content.ChoiceContent"]


# --- restJson1 ser/de ---
def serialize_json(value: Urls) -> list:
    import capo_wellarchitected.types.choice_content

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.choice_content.serialize_json(item))
    return out


def deserialize_json(data: list) -> Urls:
    import capo_wellarchitected.types.choice_content

    out: Urls = []
    for item in data:
        out.append(capo_wellarchitected.types.choice_content.deserialize_json(item))
    return out
