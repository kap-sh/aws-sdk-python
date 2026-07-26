"""Generated from Smithy shape ``com.amazonaws.elementalinference#UpdateOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.update_output

UpdateOutputList: TypeAlias = list[
    "capo_elementalinference.types.update_output.UpdateOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOutputList) -> list:
    import capo_elementalinference.types.update_output

    out: list = []
    for item in value:
        out.append(capo_elementalinference.types.update_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateOutputList:
    import capo_elementalinference.types.update_output

    out: UpdateOutputList = []
    for item in data:
        out.append(capo_elementalinference.types.update_output.deserialize_json(item))
    return out
