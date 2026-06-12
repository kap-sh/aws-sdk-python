"""Generated from Smithy shape ``com.amazonaws.glue#ComputeEnvironment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ComputeEnvironment: TypeAlias = Literal[
    "SPARK",
    "ATHENA",
    "PYTHON",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SPARK",
        "ATHENA",
        "PYTHON",
    )
)


def serialize_aws_json_1_1(value: ComputeEnvironment) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComputeEnvironment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputeEnvironment value: {data!r}")
    return cast(ComputeEnvironment, data)
