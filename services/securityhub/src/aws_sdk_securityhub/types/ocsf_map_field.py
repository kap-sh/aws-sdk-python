"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfMapField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

OcsfMapField: TypeAlias = Literal[
    "resources.tags",
    "compliance.control_parameters",
    "databucket.tags",
    "finding_info.tags",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "resources.tags",
        "compliance.control_parameters",
        "databucket.tags",
        "finding_info.tags",
    )
)


def serialize_json(value: OcsfMapField) -> str:
    return value


def deserialize_json(data: str) -> OcsfMapField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OcsfMapField value: {data!r}")
    return cast(OcsfMapField, data)
