"""Generated from Smithy shape ``com.amazonaws.servicequotas#MetricDimensionsMapDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.metric_dimension_name
    import aws_sdk_service_quotas.types.metric_dimension_value

MetricDimensionsMapDefinition: TypeAlias = dict[
    "aws_sdk_service_quotas.types.metric_dimension_name.MetricDimensionName",
    "aws_sdk_service_quotas.types.metric_dimension_value.MetricDimensionValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: MetricDimensionsMapDefinition) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricDimensionsMapDefinition:
    out: MetricDimensionsMapDefinition = {}
    for key, value in data.items():
        out[key] = value
    return out
