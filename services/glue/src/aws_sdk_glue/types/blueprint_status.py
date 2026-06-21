"""Generated from Smithy shape ``com.amazonaws.glue#BlueprintStatus``."""

from typing import Literal, TypeAlias, cast

BlueprintStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueprintStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlueprintStatus:
    return cast(BlueprintStatus, data)
