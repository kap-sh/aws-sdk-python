"""Generated from Smithy shape ``com.amazonaws.macie2#RelationshipStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: RelationshipStatus) -> str:
    return value


def deserialize_json(data: str) -> RelationshipStatus:
    return cast(RelationshipStatus, data)
