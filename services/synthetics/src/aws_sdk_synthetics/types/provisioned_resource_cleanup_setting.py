"""Generated from Smithy shape ``com.amazonaws.synthetics#ProvisionedResourceCleanupSetting``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_synthetics.errors import DeserializationError

ProvisionedResourceCleanupSetting: TypeAlias = Literal[
    "AUTOMATIC",
    "OFF",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "OFF",
    )
)


def serialize_json(value: ProvisionedResourceCleanupSetting) -> str:
    return value


def deserialize_json(data: str) -> ProvisionedResourceCleanupSetting:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProvisionedResourceCleanupSetting value: {data!r}"
        )
    return cast(ProvisionedResourceCleanupSetting, data)
