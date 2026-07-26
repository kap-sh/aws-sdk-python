"""Generated from Smithy shape ``com.amazonaws.repostspace#VanityDomainStatus``."""

from typing import Literal, TypeAlias, cast

VanityDomainStatus: TypeAlias = Literal[
    "PENDING",
    "APPROVED",
    "UNAPPROVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: VanityDomainStatus) -> str:
    return value


def deserialize_json(data: str) -> VanityDomainStatus:
    return cast(VanityDomainStatus, data)
