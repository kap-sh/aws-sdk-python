"""Generated from Smithy shape ``com.amazonaws.iot#PercentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.percent

PercentList: TypeAlias = list["aws_sdk_iot.types.percent.Percent"]


# --- restJson1 ser/de ---
def serialize_json(value: PercentList) -> list:
    return list(value)


def deserialize_json(data: list) -> PercentList:
    return list(data)
