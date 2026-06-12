"""Generated from Smithy shape ``com.amazonaws.wafv2#PathStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.path_statistics

PathStatisticsList: TypeAlias = list[
    "aws_sdk_wafv2.types.path_statistics.PathStatistics"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PathStatisticsList) -> list:
    import aws_sdk_wafv2.types.path_statistics

    out: list = []
    for item in value:
        out.append(aws_sdk_wafv2.types.path_statistics.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PathStatisticsList:
    import aws_sdk_wafv2.types.path_statistics

    out: PathStatisticsList = []
    for item in data:
        out.append(aws_sdk_wafv2.types.path_statistics.deserialize_aws_json_1_1(item))
    return out
