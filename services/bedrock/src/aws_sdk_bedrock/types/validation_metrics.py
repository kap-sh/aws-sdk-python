"""Generated from Smithy shape ``com.amazonaws.bedrock#ValidationMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.validator_metric

ValidationMetrics: TypeAlias = list[
    "aws_sdk_bedrock.types.validator_metric.ValidatorMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationMetrics) -> list:
    import aws_sdk_bedrock.types.validator_metric

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.validator_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValidationMetrics:
    import aws_sdk_bedrock.types.validator_metric

    out: ValidationMetrics = []
    for item in data:
        out.append(aws_sdk_bedrock.types.validator_metric.deserialize_json(item))
    return out
