"""Generated from Smithy shape ``com.amazonaws.macie2#AutomatedDiscoveryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The status of the automated sensitive data discovery configuration for an organization in Amazon Macie or a standalone Macie account. Valid values are:</p>"""
AutomatedDiscoveryStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: AutomatedDiscoveryStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomatedDiscoveryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutomatedDiscoveryStatus value: {data!r}")
    return cast(AutomatedDiscoveryStatus, data)
