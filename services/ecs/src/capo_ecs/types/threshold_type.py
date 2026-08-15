"""Generated from Smithy shape ``com.amazonaws.ecs#ThresholdType``."""

from typing import Literal, TypeAlias, cast

"""<p>Determines how the deployment circuit breaker calculates the number of task failures tolerated before it triggers, based on the configured <code>value</code>.</p>"""
ThresholdType: TypeAlias = Literal[
    "COUNT",
    "BOUNDED_PERCENT",
    "UNBOUNDED_PERCENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThresholdType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThresholdType:
    return cast(ThresholdType, data)
