"""Generated from Smithy shape ``com.amazonaws.securityagent#UserRole``."""

from typing import Literal, TypeAlias, cast

"""<p>Role of a user member associated to an agent space.</p>"""
UserRole: TypeAlias = Literal["MEMBER",]


# --- restJson1 ser/de ---
def serialize_json(value: UserRole) -> str:
    return value


def deserialize_json(data: str) -> UserRole:
    return cast(UserRole, data)
