"""Generated from Smithy shape ``com.amazonaws.repostspace#VanityDomainStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_repostspace.errors import DeserializationError

VanityDomainStatus: TypeAlias = Literal[
    "PENDING",
    "APPROVED",
    "UNAPPROVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "APPROVED",
        "UNAPPROVED",
    )
)


def serialize_json(value: VanityDomainStatus) -> str:
    return value


def deserialize_json(data: str) -> VanityDomainStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VanityDomainStatus value: {data!r}")
    return cast(VanityDomainStatus, data)
