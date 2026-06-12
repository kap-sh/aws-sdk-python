"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityHubFeature``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

SecurityHubFeature: TypeAlias = Literal[
    "SecurityHub",
    "SecurityHubV2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SecurityHub",
        "SecurityHubV2",
    )
)


def serialize_json(value: SecurityHubFeature) -> str:
    return value


def deserialize_json(data: str) -> SecurityHubFeature:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SecurityHubFeature value: {data!r}")
    return cast(SecurityHubFeature, data)
