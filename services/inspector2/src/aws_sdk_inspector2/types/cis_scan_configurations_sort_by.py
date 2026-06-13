"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanConfigurationsSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisScanConfigurationsSortBy: TypeAlias = Literal[
    "SCAN_NAME",
    "SCAN_CONFIGURATION_ARN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCAN_NAME",
        "SCAN_CONFIGURATION_ARN",
    )
)


def serialize_json(value: CisScanConfigurationsSortBy) -> str:
    return value


def deserialize_json(data: str) -> CisScanConfigurationsSortBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CisScanConfigurationsSortBy value: {data!r}"
        )
    return cast(CisScanConfigurationsSortBy, data)
