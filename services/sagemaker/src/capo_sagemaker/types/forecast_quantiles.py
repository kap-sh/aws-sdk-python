"""Generated from Smithy shape ``com.amazonaws.sagemaker#ForecastQuantiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.forecast_quantile

ForecastQuantiles: TypeAlias = list[
    "capo_sagemaker.types.forecast_quantile.ForecastQuantile"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForecastQuantiles) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ForecastQuantiles:
    return list(data)
