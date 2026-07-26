"""Generated from Smithy shape ``com.amazonaws.quicksight#StringDefaultValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_string_object

StringDefaultValueList: TypeAlias = list[
    "capo_quicksight.types.sensitive_string_object.SensitiveStringObject"
]


# --- restJson1 ser/de ---
def serialize_json(value: StringDefaultValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringDefaultValueList:
    return list(data)
