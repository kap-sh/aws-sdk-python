"""Generated from Smithy shape ``com.amazonaws.macie2#RelationshipStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The current status of the relationship between an account and an associated Amazon Macie administrator account. Possible values are:</p>"""
RelationshipStatus: TypeAlias = Literal[
    "Enabled",
    "Paused",
    "Invited",
    "Created",
    "Removed",
    "Resigned",
    "EmailVerificationInProgress",
    "EmailVerificationFailed",
    "RegionDisabled",
    "AccountSuspended",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Paused",
        "Invited",
        "Created",
        "Removed",
        "Resigned",
        "EmailVerificationInProgress",
        "EmailVerificationFailed",
        "RegionDisabled",
        "AccountSuspended",
    )
)


def serialize_json(value: RelationshipStatus) -> str:
    return value


def deserialize_json(data: str) -> RelationshipStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RelationshipStatus value: {data!r}")
    return cast(RelationshipStatus, data)
