"""Generated from Smithy shape ``com.amazonaws.ssm#OpsFilterOperatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

OpsFilterOperatorType: TypeAlias = Literal[
    "Equal",
    "NotEqual",
    "BeginWith",
    "LessThan",
    "GreaterThan",
    "Exists",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Equal",
        "NotEqual",
        "BeginWith",
        "LessThan",
        "GreaterThan",
        "Exists",
    )
)


def serialize_aws_json_1_1(value: OpsFilterOperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsFilterOperatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpsFilterOperatorType value: {data!r}")
    return cast(OpsFilterOperatorType, data)
