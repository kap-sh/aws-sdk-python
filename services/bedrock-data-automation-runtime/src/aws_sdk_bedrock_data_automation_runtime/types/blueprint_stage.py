"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#BlueprintStage``."""

from typing import Literal, TypeAlias, cast

"""Blueprint stage enum."""
BlueprintStage: TypeAlias = Literal[
    "DEVELOPMENT",
    "LIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueprintStage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlueprintStage:
    return cast(BlueprintStage, data)
