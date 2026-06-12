"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesDateField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ResourcesDateField: TypeAlias = Literal[
    "ResourceDetailCaptureTime",
    "ResourceCreationTime",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ResourceDetailCaptureTime",
        "ResourceCreationTime",
    )
)


def serialize_json(value: ResourcesDateField) -> str:
    return value


def deserialize_json(data: str) -> ResourcesDateField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourcesDateField value: {data!r}")
    return cast(ResourcesDateField, data)
