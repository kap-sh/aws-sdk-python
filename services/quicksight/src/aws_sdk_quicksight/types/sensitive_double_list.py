"""Generated from Smithy shape ``com.amazonaws.quicksight#SensitiveDoubleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sensitive_double

SensitiveDoubleList: TypeAlias = list[
    "aws_sdk_quicksight.types.sensitive_double.SensitiveDouble"
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveDoubleList) -> list:
    return list(value)


def deserialize_json(data: list) -> SensitiveDoubleList:
    return list(data)
