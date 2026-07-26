"""Generated from Smithy shape ``com.amazonaws.securityhub#ActorSessionMfaStatus``."""

from typing import Literal, TypeAlias, cast

ActorSessionMfaStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActorSessionMfaStatus) -> str:
    return value


def deserialize_json(data: str) -> ActorSessionMfaStatus:
    return cast(ActorSessionMfaStatus, data)
