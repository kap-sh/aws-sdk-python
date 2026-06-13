"""Generated from Smithy shape ``com.amazonaws.securityagent#UserRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Role of a user member associated to an agent space.</p>"""
UserRole: TypeAlias = Literal["MEMBER",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MEMBER",))


def serialize_json(value: UserRole) -> str:
    return value


def deserialize_json(data: str) -> UserRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserRole value: {data!r}")
    return cast(UserRole, data)
