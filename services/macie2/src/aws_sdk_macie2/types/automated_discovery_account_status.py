"""Generated from Smithy shape ``com.amazonaws.macie2#AutomatedDiscoveryAccountStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The status of automated sensitive data discovery for an Amazon Macie account. Valid values are:</p>"""
AutomatedDiscoveryAccountStatus: TypeAlias = Literal[
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


def serialize_json(value: AutomatedDiscoveryAccountStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomatedDiscoveryAccountStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedDiscoveryAccountStatus value: {data!r}"
        )
    return cast(AutomatedDiscoveryAccountStatus, data)
