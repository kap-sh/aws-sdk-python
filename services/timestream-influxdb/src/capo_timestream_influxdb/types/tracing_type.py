"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#TracingType``."""

from typing import Literal, TypeAlias, cast

TracingType: TypeAlias = Literal[
    "log",
    "jaeger",
    "disabled",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TracingType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TracingType:
    return cast(TracingType, data)
