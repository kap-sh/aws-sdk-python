"""Generated from Smithy shape ``com.amazonaws.licensemanager#InventoryFilterCondition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

InventoryFilterCondition: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "BEGINS_WITH",
    "CONTAINS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "NOT_EQUALS",
        "BEGINS_WITH",
        "CONTAINS",
    )
)


def serialize_aws_json_1_1(value: InventoryFilterCondition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InventoryFilterCondition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InventoryFilterCondition value: {data!r}")
    return cast(InventoryFilterCondition, data)
