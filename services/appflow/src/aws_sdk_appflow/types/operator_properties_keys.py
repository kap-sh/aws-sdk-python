"""Generated from Smithy shape ``com.amazonaws.appflow#OperatorPropertiesKeys``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

OperatorPropertiesKeys: TypeAlias = Literal[
    "VALUE",
    "VALUES",
    "DATA_TYPE",
    "UPPER_BOUND",
    "LOWER_BOUND",
    "SOURCE_DATA_TYPE",
    "DESTINATION_DATA_TYPE",
    "VALIDATION_ACTION",
    "MASK_VALUE",
    "MASK_LENGTH",
    "TRUNCATE_LENGTH",
    "MATH_OPERATION_FIELDS_ORDER",
    "CONCAT_FORMAT",
    "SUBFIELD_CATEGORY_MAP",
    "EXCLUDE_SOURCE_FIELDS_LIST",
    "INCLUDE_NEW_FIELDS",
    "ORDERED_PARTITION_KEYS_LIST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALUE",
        "VALUES",
        "DATA_TYPE",
        "UPPER_BOUND",
        "LOWER_BOUND",
        "SOURCE_DATA_TYPE",
        "DESTINATION_DATA_TYPE",
        "VALIDATION_ACTION",
        "MASK_VALUE",
        "MASK_LENGTH",
        "TRUNCATE_LENGTH",
        "MATH_OPERATION_FIELDS_ORDER",
        "CONCAT_FORMAT",
        "SUBFIELD_CATEGORY_MAP",
        "EXCLUDE_SOURCE_FIELDS_LIST",
        "INCLUDE_NEW_FIELDS",
        "ORDERED_PARTITION_KEYS_LIST",
    )
)


def serialize_json(value: OperatorPropertiesKeys) -> str:
    return value


def deserialize_json(data: str) -> OperatorPropertiesKeys:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperatorPropertiesKeys value: {data!r}")
    return cast(OperatorPropertiesKeys, data)
