"""Generated from Smithy shape ``com.amazonaws.macie2#UserIdentityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The type of entity that performed the action on the affected resource. Possible values are:</p>"""
UserIdentityType: TypeAlias = Literal[
    "AssumedRole",
    "IAMUser",
    "FederatedUser",
    "Root",
    "AWSAccount",
    "AWSService",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AssumedRole",
        "IAMUser",
        "FederatedUser",
        "Root",
        "AWSAccount",
        "AWSService",
    )
)


def serialize_json(value: UserIdentityType) -> str:
    return value


def deserialize_json(data: str) -> UserIdentityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserIdentityType value: {data!r}")
    return cast(UserIdentityType, data)
