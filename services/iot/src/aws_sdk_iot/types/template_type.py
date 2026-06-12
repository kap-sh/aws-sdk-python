"""Generated from Smithy shape ``com.amazonaws.iot#TemplateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

TemplateType: TypeAlias = Literal[
    "FLEET_PROVISIONING",
    "JITP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FLEET_PROVISIONING",
        "JITP",
    )
)


def serialize_json(value: TemplateType) -> str:
    return value


def deserialize_json(data: str) -> TemplateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TemplateType value: {data!r}")
    return cast(TemplateType, data)
