"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesTrendsStringField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ResourcesTrendsStringField: TypeAlias = Literal[
    "account_id",
    "region",
    "resource_type",
    "resource_category",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "account_id",
        "region",
        "resource_type",
        "resource_category",
    )
)


def serialize_json(value: ResourcesTrendsStringField) -> str:
    return value


def deserialize_json(data: str) -> ResourcesTrendsStringField:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourcesTrendsStringField value: {data!r}"
        )
    return cast(ResourcesTrendsStringField, data)
