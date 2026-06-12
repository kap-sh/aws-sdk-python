"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryAttributeDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

InventoryAttributeDataType: TypeAlias = Literal[
    "string",
    "number",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "string",
        "number",
    )
)


def serialize_aws_json_1_1(value: InventoryAttributeDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InventoryAttributeDataType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InventoryAttributeDataType value: {data!r}"
        )
    return cast(InventoryAttributeDataType, data)
