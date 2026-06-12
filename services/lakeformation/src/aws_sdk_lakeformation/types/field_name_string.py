"""Generated from Smithy shape ``com.amazonaws.lakeformation#FieldNameString``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

FieldNameString: TypeAlias = Literal[
    "RESOURCE_ARN",
    "ROLE_ARN",
    "LAST_MODIFIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESOURCE_ARN",
        "ROLE_ARN",
        "LAST_MODIFIED",
    )
)


def serialize_json(value: FieldNameString) -> str:
    return value


def deserialize_json(data: str) -> FieldNameString:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FieldNameString value: {data!r}")
    return cast(FieldNameString, data)
