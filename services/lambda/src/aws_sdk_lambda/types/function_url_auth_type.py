"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionUrlAuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

FunctionUrlAuthType: TypeAlias = Literal[
    "NONE",
    "AWS_IAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "AWS_IAM",
    )
)


def serialize_json(value: FunctionUrlAuthType) -> str:
    return value


def deserialize_json(data: str) -> FunctionUrlAuthType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FunctionUrlAuthType value: {data!r}")
    return cast(FunctionUrlAuthType, data)
