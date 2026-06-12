"""Generated from Smithy shape ``com.amazonaws.guardduty#PublicAclIgnoreBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

PublicAclIgnoreBehavior: TypeAlias = Literal[
    "IGNORED",
    "NOT_IGNORED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IGNORED",
        "NOT_IGNORED",
    )
)


def serialize_json(value: PublicAclIgnoreBehavior) -> str:
    return value


def deserialize_json(data: str) -> PublicAclIgnoreBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PublicAclIgnoreBehavior value: {data!r}")
    return cast(PublicAclIgnoreBehavior, data)
