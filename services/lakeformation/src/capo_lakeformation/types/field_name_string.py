"""Generated from Smithy shape ``com.amazonaws.lakeformation#FieldNameString``."""

from typing import Literal, TypeAlias, cast

FieldNameString: TypeAlias = Literal[
    "RESOURCE_ARN",
    "ROLE_ARN",
    "LAST_MODIFIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FieldNameString) -> str:
    return value


def deserialize_json(data: str) -> FieldNameString:
    return cast(FieldNameString, data)
