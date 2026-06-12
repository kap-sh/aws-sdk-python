"""Generated from Smithy shape ``com.amazonaws.customerprofiles#TrainingMetricsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.training_metrics

TrainingMetricsList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.training_metrics.TrainingMetrics"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrainingMetricsList) -> list:
    import aws_sdk_customer_profiles.types.training_metrics

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.training_metrics.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TrainingMetricsList:
    import aws_sdk_customer_profiles.types.training_metrics

    out: TrainingMetricsList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.training_metrics.deserialize_json(item)
        )
    return out
