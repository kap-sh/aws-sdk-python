"""Generated from Smithy shape ``com.amazonaws.ecs#ScaleUnit``."""

from typing import Literal, TypeAlias, cast

ScaleUnit: TypeAlias = Literal["PERCENT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScaleUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScaleUnit:
    return cast(ScaleUnit, data)
