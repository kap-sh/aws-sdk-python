"""Generated from Smithy shape ``com.amazonaws.amplify#WafStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplify.errors import DeserializationError

WafStatus: TypeAlias = Literal[
    "ASSOCIATING",
    "ASSOCIATION_FAILED",
    "ASSOCIATION_SUCCESS",
    "DISASSOCIATING",
    "DISASSOCIATION_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSOCIATING",
        "ASSOCIATION_FAILED",
        "ASSOCIATION_SUCCESS",
        "DISASSOCIATING",
        "DISASSOCIATION_FAILED",
    )
)


def serialize_json(value: WafStatus) -> str:
    return value


def deserialize_json(data: str) -> WafStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WafStatus value: {data!r}")
    return cast(WafStatus, data)
