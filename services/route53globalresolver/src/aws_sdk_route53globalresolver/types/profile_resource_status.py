"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ProfileResourceStatus``."""

from typing import Literal, TypeAlias, cast

ProfileResourceStatus: TypeAlias = Literal[
    "CREATING",
    "OPERATIONAL",
    "UPDATING",
    "ENABLING",
    "DISABLING",
    "DISABLED",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> ProfileResourceStatus:
    return cast(ProfileResourceStatus, data)
