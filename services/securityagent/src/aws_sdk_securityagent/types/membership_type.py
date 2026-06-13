"""Generated from Smithy shape ``com.amazonaws.securityagent#MembershipType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Type of membership.</p>"""
MembershipType: TypeAlias = Literal["USER",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("USER",))


def serialize_json(value: MembershipType) -> str:
    return value


def deserialize_json(data: str) -> MembershipType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MembershipType value: {data!r}")
    return cast(MembershipType, data)
