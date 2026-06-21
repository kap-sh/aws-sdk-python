"""Generated from Smithy shape ``com.amazonaws.route53profiles#ProfileStatus``."""

from typing import Literal, TypeAlias, cast

ProfileStatus: TypeAlias = Literal[
    "COMPLETE",
    "DELETING",
    "UPDATING",
    "CREATING",
    "DELETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> ProfileStatus:
    return cast(ProfileStatus, data)
