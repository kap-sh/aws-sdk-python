"""Generated from Smithy shape ``com.amazonaws.lightsail#BlueprintType``."""

from typing import Literal, TypeAlias, cast

BlueprintType: TypeAlias = Literal[
    "os",
    "app",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueprintType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlueprintType:
    return cast(BlueprintType, data)
