"""Generated from Smithy shape ``com.amazonaws.quicksight#DecimalDefaultValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_double_object

DecimalDefaultValueList: TypeAlias = list[
    "capo_quicksight.types.sensitive_double_object.SensitiveDoubleObject"
]


# --- restJson1 ser/de ---
def serialize_json(value: DecimalDefaultValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> DecimalDefaultValueList:
    return list(data)
