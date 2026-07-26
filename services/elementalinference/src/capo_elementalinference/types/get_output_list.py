"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.get_output

GetOutputList: TypeAlias = list["capo_elementalinference.types.get_output.GetOutput"]


# --- restJson1 ser/de ---
def serialize_json(value: GetOutputList) -> list:
    import capo_elementalinference.types.get_output

    out: list = []
    for item in value:
        out.append(capo_elementalinference.types.get_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> GetOutputList:
    import capo_elementalinference.types.get_output

    out: GetOutputList = []
    for item in data:
        out.append(capo_elementalinference.types.get_output.deserialize_json(item))
    return out
