"""Generated from Smithy shape ``com.amazonaws.ssm#ExecutionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ExecutionMode: TypeAlias = Literal[
    "Auto",
    "Interactive",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Auto",
        "Interactive",
    )
)


def serialize_aws_json_1_1(value: ExecutionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionMode value: {data!r}")
    return cast(ExecutionMode, data)
