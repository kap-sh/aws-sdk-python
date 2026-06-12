"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#TokenStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53globalresolver.errors import DeserializationError

TokenStatus: TypeAlias = Literal[
    "CREATING",
    "OPERATIONAL",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "OPERATIONAL",
        "DELETING",
    )
)


def serialize_json(value: TokenStatus) -> str:
    return value


def deserialize_json(data: str) -> TokenStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TokenStatus value: {data!r}")
    return cast(TokenStatus, data)
