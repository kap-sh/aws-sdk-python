"""Generated from Smithy shape ``com.amazonaws.route53profiles#ShareStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53profiles.errors import DeserializationError

ShareStatus: TypeAlias = Literal[
    "NOT_SHARED",
    "SHARED_WITH_ME",
    "SHARED_BY_ME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_SHARED",
        "SHARED_WITH_ME",
        "SHARED_BY_ME",
    )
)


def serialize_json(value: ShareStatus) -> str:
    return value


def deserialize_json(data: str) -> ShareStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShareStatus value: {data!r}")
    return cast(ShareStatus, data)
