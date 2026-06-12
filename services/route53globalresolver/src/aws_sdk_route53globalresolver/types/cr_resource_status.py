"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CRResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53globalresolver.errors import DeserializationError

CRResourceStatus: TypeAlias = Literal[
    "CREATING",
    "OPERATIONAL",
    "UPDATING",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "OPERATIONAL",
        "UPDATING",
        "DELETING",
    )
)


def serialize_json(value: CRResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> CRResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CRResourceStatus value: {data!r}")
    return cast(CRResourceStatus, data)
