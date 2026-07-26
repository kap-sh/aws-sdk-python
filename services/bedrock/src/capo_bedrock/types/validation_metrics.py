"""Generated from Smithy shape ``com.amazonaws.bedrock#ValidationMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.validator_metric

ValidationMetrics: TypeAlias = list[
    "capo_bedrock.types.validator_metric.ValidatorMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationMetrics) -> list:
    import capo_bedrock.types.validator_metric

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.validator_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValidationMetrics:
    import capo_bedrock.types.validator_metric

    out: ValidationMetrics = []
    for item in data:
        out.append(capo_bedrock.types.validator_metric.deserialize_json(item))
    return out
