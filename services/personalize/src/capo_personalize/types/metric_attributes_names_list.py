"""Generated from Smithy shape ``com.amazonaws.personalize#MetricAttributesNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.metric_name

MetricAttributesNamesList: TypeAlias = list[
    "capo_personalize.types.metric_name.MetricName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricAttributesNamesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MetricAttributesNamesList:
    return list(data)
