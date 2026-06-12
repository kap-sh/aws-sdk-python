"""Generated from Smithy shape ``com.amazonaws.glacier#Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glacier.errors import DeserializationError

Type: TypeAlias = Literal[
    "AmazonCustomerByEmail",
    "CanonicalUser",
    "Group",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AmazonCustomerByEmail",
        "CanonicalUser",
        "Group",
    )
)


def serialize_json(value: Type) -> str:
    return value


def deserialize_json(data: str) -> Type:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Type value: {data!r}")
    return cast(Type, data)
