"""Generated from Smithy shape ``com.amazonaws.costexplorer#ForecastResultsByTime``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.forecast_result

ForecastResultsByTime: TypeAlias = list[
    "aws_sdk_cost_explorer.types.forecast_result.ForecastResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForecastResultsByTime) -> list:
    import aws_sdk_cost_explorer.types.forecast_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.forecast_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ForecastResultsByTime:
    import aws_sdk_cost_explorer.types.forecast_result

    out: ForecastResultsByTime = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.forecast_result.deserialize_aws_json_1_1(item)
        )
    return out
