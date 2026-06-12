"""Generated from Smithy shape ``com.amazonaws.forecast#WeightedQuantileLosses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.weighted_quantile_loss

WeightedQuantileLosses: TypeAlias = list[
    "aws_sdk_forecast.types.weighted_quantile_loss.WeightedQuantileLoss"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WeightedQuantileLosses) -> list:
    import aws_sdk_forecast.types.weighted_quantile_loss

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.weighted_quantile_loss.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WeightedQuantileLosses:
    import aws_sdk_forecast.types.weighted_quantile_loss

    out: WeightedQuantileLosses = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.weighted_quantile_loss.deserialize_aws_json_1_1(item)
        )
    return out
