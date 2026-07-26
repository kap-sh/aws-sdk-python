"""Generated from Smithy shape ``com.amazonaws.guardduty#PublicAccessStatus``."""

from typing import Literal, TypeAlias, cast

PublicAccessStatus: TypeAlias = Literal[
    "BLOCKED",
    "ALLOWED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PublicAccessStatus) -> str:
    return value


def deserialize_json(data: str) -> PublicAccessStatus:
    return cast(PublicAccessStatus, data)
