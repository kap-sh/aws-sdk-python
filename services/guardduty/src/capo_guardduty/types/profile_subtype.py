"""Generated from Smithy shape ``com.amazonaws.guardduty#ProfileSubtype``."""

from typing import Literal, TypeAlias, cast

ProfileSubtype: TypeAlias = Literal[
    "FREQUENT",
    "INFREQUENT",
    "UNSEEN",
    "RARE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileSubtype) -> str:
    return value


def deserialize_json(data: str) -> ProfileSubtype:
    return cast(ProfileSubtype, data)
