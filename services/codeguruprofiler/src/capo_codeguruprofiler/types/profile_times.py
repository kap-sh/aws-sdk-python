"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ProfileTimes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.profile_time

ProfileTimes: TypeAlias = list["capo_codeguruprofiler.types.profile_time.ProfileTime"]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileTimes) -> list:
    import capo_codeguruprofiler.types.profile_time

    out: list = []
    for item in value:
        out.append(capo_codeguruprofiler.types.profile_time.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileTimes:
    import capo_codeguruprofiler.types.profile_time

    out: ProfileTimes = []
    for item in data:
        out.append(capo_codeguruprofiler.types.profile_time.deserialize_json(item))
    return out
