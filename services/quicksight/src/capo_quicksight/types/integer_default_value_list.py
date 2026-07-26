"""Generated from Smithy shape ``com.amazonaws.quicksight#IntegerDefaultValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_long_object

IntegerDefaultValueList: TypeAlias = list[
    "capo_quicksight.types.sensitive_long_object.SensitiveLongObject"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegerDefaultValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> IntegerDefaultValueList:
    return list(data)
