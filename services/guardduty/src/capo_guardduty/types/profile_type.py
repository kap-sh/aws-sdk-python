"""Generated from Smithy shape ``com.amazonaws.guardduty#ProfileType``."""

from typing import Literal, TypeAlias, cast

ProfileType: TypeAlias = Literal["FREQUENCY",]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileType) -> str:
    return value


def deserialize_json(data: str) -> ProfileType:
    return cast(ProfileType, data)
