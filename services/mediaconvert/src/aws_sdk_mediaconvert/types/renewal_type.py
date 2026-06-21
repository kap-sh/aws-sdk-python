"""Generated from Smithy shape ``com.amazonaws.mediaconvert#RenewalType``."""

from typing import Literal, TypeAlias, cast

"""Specifies whether the term of your reserved queue pricing plan is automatically extended (AUTO_RENEW) or expires (EXPIRE) at the end of the term."""
RenewalType: TypeAlias = Literal[
    "AUTO_RENEW",
    "EXPIRE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RenewalType) -> str:
    return value


def deserialize_json(data: str) -> RenewalType:
    return cast(RenewalType, data)
