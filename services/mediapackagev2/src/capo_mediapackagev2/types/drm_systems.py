"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DrmSystems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.drm_system

DrmSystems: TypeAlias = list["capo_mediapackagev2.types.drm_system.DrmSystem"]


# --- restJson1 ser/de ---
def serialize_json(value: DrmSystems) -> list:
    import capo_mediapackagev2.types.drm_system

    out: list = []
    for item in value:
        out.append(capo_mediapackagev2.types.drm_system.serialize_json(item))
    return out


def deserialize_json(data: list) -> DrmSystems:
    import capo_mediapackagev2.types.drm_system

    out: DrmSystems = []
    for item in data:
        out.append(capo_mediapackagev2.types.drm_system.deserialize_json(item))
    return out
