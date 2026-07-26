"""Generated from Smithy shape ``com.amazonaws.quicksight#StringParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.string_parameter

StringParameterList: TypeAlias = list[
    "capo_quicksight.types.string_parameter.StringParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: StringParameterList) -> list:
    import capo_quicksight.types.string_parameter

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.string_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> StringParameterList:
    import capo_quicksight.types.string_parameter

    out: StringParameterList = []
    for item in data:
        out.append(capo_quicksight.types.string_parameter.deserialize_json(item))
    return out
