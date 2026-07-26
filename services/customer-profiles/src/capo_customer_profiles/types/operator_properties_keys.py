"""Generated from Smithy shape ``com.amazonaws.customerprofiles#OperatorPropertiesKeys``."""

from typing import Literal, TypeAlias, cast

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
]


# --- restJson1 ser/de ---
def serialize_json(value: OperatorPropertiesKeys) -> str:
    return value


def deserialize_json(data: str) -> OperatorPropertiesKeys:
    return cast(OperatorPropertiesKeys, data)
