"""Generated from Smithy shape ``com.amazonaws.connect#MonthList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.month

MonthList: TypeAlias = list["aws_sdk_connect.types.month.Month"]


# --- restJson1 ser/de ---
def serialize_json(value: MonthList) -> list:
    return list(value)


def deserialize_json(data: list) -> MonthList:
    return list(data)
