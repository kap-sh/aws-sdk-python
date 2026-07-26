"""Generated from Smithy shape ``com.amazonaws.personalize#MetricAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.metric_attribute

MetricAttributes: TypeAlias = list[
    "capo_personalize.types.metric_attribute.MetricAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricAttributes) -> list:
    import capo_personalize.types.metric_attribute

    out: list = []
    for item in value:
        out.append(capo_personalize.types.metric_attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetricAttributes:
    import capo_personalize.types.metric_attribute

    out: MetricAttributes = []
    for item in data:
        out.append(
            capo_personalize.types.metric_attribute.deserialize_aws_json_1_1(item)
        )
    return out
