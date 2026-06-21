"""Generated from Smithy shape ``com.amazonaws.route53profiles#ShareStatus``."""

from typing import Literal, TypeAlias, cast

ShareStatus: TypeAlias = Literal[
    "NOT_SHARED",
    "SHARED_WITH_ME",
    "SHARED_BY_ME",
]


# --- restJson1 ser/de ---
def serialize_json(value: ShareStatus) -> str:
    return value


def deserialize_json(data: str) -> ShareStatus:
    return cast(ShareStatus, data)
