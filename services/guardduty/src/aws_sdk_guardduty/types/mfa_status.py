"""Generated from Smithy shape ``com.amazonaws.guardduty#MfaStatus``."""

from typing import Literal, TypeAlias, cast

MfaStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MfaStatus) -> str:
    return value


def deserialize_json(data: str) -> MfaStatus:
    return cast(MfaStatus, data)
