"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

OpsItemFilterOperator: TypeAlias = Literal[
    "Equal",
    "Contains",
    "GreaterThan",
    "LessThan",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Equal",
        "Contains",
        "GreaterThan",
        "LessThan",
    )
)


def serialize_aws_json_1_1(value: OpsItemFilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpsItemFilterOperator value: {data!r}")
    return cast(OpsItemFilterOperator, data)
