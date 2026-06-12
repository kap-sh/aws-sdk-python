"""Generated from Smithy shape ``com.amazonaws.codedeploy#ComputePlatform``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

ComputePlatform: TypeAlias = Literal[
    "Server",
    "Lambda",
    "ECS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Server",
        "Lambda",
        "ECS",
    )
)


def serialize_aws_json_1_1(value: ComputePlatform) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComputePlatform:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputePlatform value: {data!r}")
    return cast(ComputePlatform, data)
