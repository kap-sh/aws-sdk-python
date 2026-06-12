"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ShareStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

"""<p>The status of the share request.</p>"""
ShareStatus: TypeAlias = Literal[
    "ACCEPTED",
    "REJECTED",
    "PENDING",
    "REVOKED",
    "EXPIRED",
    "ASSOCIATING",
    "ASSOCIATED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCEPTED",
        "REJECTED",
        "PENDING",
        "REVOKED",
        "EXPIRED",
        "ASSOCIATING",
        "ASSOCIATED",
        "FAILED",
    )
)


def serialize_json(value: ShareStatus) -> str:
    return value


def deserialize_json(data: str) -> ShareStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShareStatus value: {data!r}")
    return cast(ShareStatus, data)
