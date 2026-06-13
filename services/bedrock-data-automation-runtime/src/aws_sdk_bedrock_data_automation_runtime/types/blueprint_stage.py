"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#BlueprintStage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError

"""Blueprint stage enum."""
BlueprintStage: TypeAlias = Literal[
    "DEVELOPMENT",
    "LIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEVELOPMENT",
        "LIVE",
    )
)


def serialize_aws_json_1_1(value: BlueprintStage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlueprintStage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlueprintStage value: {data!r}")
    return cast(BlueprintStage, data)
