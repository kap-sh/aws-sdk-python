"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfDateField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

OcsfDateField: TypeAlias = Literal[
    "finding_info.created_time_dt",
    "finding_info.first_seen_time_dt",
    "finding_info.last_seen_time_dt",
    "finding_info.modified_time_dt",
    "resources.image.created_time_dt",
    "resources.image.last_used_time_dt",
    "resources.modified_time_dt",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "finding_info.created_time_dt",
        "finding_info.first_seen_time_dt",
        "finding_info.last_seen_time_dt",
        "finding_info.modified_time_dt",
        "resources.image.created_time_dt",
        "resources.image.last_used_time_dt",
        "resources.modified_time_dt",
    )
)


def serialize_json(value: OcsfDateField) -> str:
    return value


def deserialize_json(data: str) -> OcsfDateField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OcsfDateField value: {data!r}")
    return cast(OcsfDateField, data)
