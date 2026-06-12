"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Metrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.double
    import aws_sdk_customer_profiles.types.training_metric_name

Metrics: TypeAlias = dict[
    "aws_sdk_customer_profiles.types.training_metric_name.TrainingMetricName",
    "aws_sdk_customer_profiles.types.double.Double",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Metrics) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_customer_profiles.types.training_metric_name

        out[
            aws_sdk_customer_profiles.types.training_metric_name.serialize_json(key)
        ] = value
    return out


def deserialize_json(data: dict) -> Metrics:
    out: Metrics = {}
    for key, value in data.items():
        import aws_sdk_customer_profiles.types.training_metric_name

        out[
            aws_sdk_customer_profiles.types.training_metric_name.deserialize_json(key)
        ] = value
    return out
