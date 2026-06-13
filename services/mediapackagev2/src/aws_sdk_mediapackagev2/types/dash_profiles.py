"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashProfiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.dash_profile

DashProfiles: TypeAlias = list["aws_sdk_mediapackagev2.types.dash_profile.DashProfile"]


# --- restJson1 ser/de ---
def serialize_json(value: DashProfiles) -> list:
    import aws_sdk_mediapackagev2.types.dash_profile

    out: list = []
    for item in value:
        out.append(aws_sdk_mediapackagev2.types.dash_profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> DashProfiles:
    import aws_sdk_mediapackagev2.types.dash_profile

    out: DashProfiles = []
    for item in data:
        out.append(aws_sdk_mediapackagev2.types.dash_profile.deserialize_json(item))
    return out
