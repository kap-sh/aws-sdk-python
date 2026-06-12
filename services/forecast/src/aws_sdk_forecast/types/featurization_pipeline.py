"""Generated from Smithy shape ``com.amazonaws.forecast#FeaturizationPipeline``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.featurization_method

FeaturizationPipeline: TypeAlias = list[
    "aws_sdk_forecast.types.featurization_method.FeaturizationMethod"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturizationPipeline) -> list:
    import aws_sdk_forecast.types.featurization_method

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.featurization_method.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FeaturizationPipeline:
    import aws_sdk_forecast.types.featurization_method

    out: FeaturizationPipeline = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.featurization_method.deserialize_aws_json_1_1(item)
        )
    return out
