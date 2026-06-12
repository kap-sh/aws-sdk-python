"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryQueryOperatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

InventoryQueryOperatorType: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: InventoryQueryOperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InventoryQueryOperatorType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InventoryQueryOperatorType value: {data!r}"
        )
    return cast(InventoryQueryOperatorType, data)
