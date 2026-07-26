"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashProfiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.dash_profile

DashProfiles: TypeAlias = list["capo_mediapackagev2.types.dash_profile.DashProfile"]


# --- restJson1 ser/de ---
def serialize_json(value: DashProfiles) -> list:
    import capo_mediapackagev2.types.dash_profile

    out: list = []
    for item in value:
        out.append(capo_mediapackagev2.types.dash_profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> DashProfiles:
    import capo_mediapackagev2.types.dash_profile

    out: DashProfiles = []
    for item in data:
        out.append(capo_mediapackagev2.types.dash_profile.deserialize_json(item))
    return out
