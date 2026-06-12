"""Generated from Smithy shape ``com.amazonaws.costexplorer#ResultsByTime``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.result_by_time

ResultsByTime: TypeAlias = list[
    "aws_sdk_cost_explorer.types.result_by_time.ResultByTime"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultsByTime) -> list:
    import aws_sdk_cost_explorer.types.result_by_time

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.result_by_time.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResultsByTime:
    import aws_sdk_cost_explorer.types.result_by_time

    out: ResultsByTime = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.result_by_time.deserialize_aws_json_1_1(item)
        )
    return out
