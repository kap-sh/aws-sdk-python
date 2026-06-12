"""Generated from Smithy shape ``com.amazonaws.databrew#AllowedStatisticList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.allowed_statistics

AllowedStatisticList: TypeAlias = list[
    "aws_sdk_databrew.types.allowed_statistics.AllowedStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedStatisticList) -> list:
    import aws_sdk_databrew.types.allowed_statistics

    out: list = []
    for item in value:
        out.append(aws_sdk_databrew.types.allowed_statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> AllowedStatisticList:
    import aws_sdk_databrew.types.allowed_statistics

    out: AllowedStatisticList = []
    for item in data:
        out.append(aws_sdk_databrew.types.allowed_statistics.deserialize_json(item))
    return out
