"""Generated from Smithy shape ``com.amazonaws.securityagent#MembershipTypeFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Filter for member type in list operations.</p>"""
MembershipTypeFilter: TypeAlias = Literal[
    "USER",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "ALL",
    )
)


def serialize_json(value: MembershipTypeFilter) -> str:
    return value


def deserialize_json(data: str) -> MembershipTypeFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MembershipTypeFilter value: {data!r}")
    return cast(MembershipTypeFilter, data)
