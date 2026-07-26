"""Generated from Smithy shape ``com.amazonaws.panorama#DeviceJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.device_job

DeviceJobList: TypeAlias = list["capo_panorama.types.device_job.DeviceJob"]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceJobList) -> list:
    import capo_panorama.types.device_job

    out: list = []
    for item in value:
        out.append(capo_panorama.types.device_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeviceJobList:
    import capo_panorama.types.device_job

    out: DeviceJobList = []
    for item in data:
        out.append(capo_panorama.types.device_job.deserialize_json(item))
    return out
