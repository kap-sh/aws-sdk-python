"""Generated from Smithy shape ``com.amazonaws.quicksight#SensitiveLongList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sensitive_long

SensitiveLongList: TypeAlias = list[
    "aws_sdk_quicksight.types.sensitive_long.SensitiveLong"
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveLongList) -> list:
    return list(value)


def deserialize_json(data: list) -> SensitiveLongList:
    return list(data)
