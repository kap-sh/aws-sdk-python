"""Generated from Smithy shape ``com.amazonaws.networkmanager#SiteState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

SiteState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "UPDATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "AVAILABLE",
        "DELETING",
        "UPDATING",
    )
)


def serialize_json(value: SiteState) -> str:
    return value


def deserialize_json(data: str) -> SiteState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SiteState value: {data!r}")
    return cast(SiteState, data)
