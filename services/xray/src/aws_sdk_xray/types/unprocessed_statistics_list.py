"""Generated from Smithy shape ``com.amazonaws.xray#UnprocessedStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.unprocessed_statistics

UnprocessedStatisticsList: TypeAlias = list[
    "aws_sdk_xray.types.unprocessed_statistics.UnprocessedStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedStatisticsList) -> list:
    import aws_sdk_xray.types.unprocessed_statistics

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.unprocessed_statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> UnprocessedStatisticsList:
    import aws_sdk_xray.types.unprocessed_statistics

    out: UnprocessedStatisticsList = []
    for item in data:
        out.append(aws_sdk_xray.types.unprocessed_statistics.deserialize_json(item))
    return out
