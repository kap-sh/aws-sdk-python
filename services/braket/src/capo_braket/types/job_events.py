"""Generated from Smithy shape ``com.amazonaws.braket#JobEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_braket.types.job_event_details

JobEvents: TypeAlias = list["capo_braket.types.job_event_details.JobEventDetails"]


# --- restJson1 ser/de ---
def serialize_json(value: JobEvents) -> list:
    import capo_braket.types.job_event_details

    out: list = []
    for item in value:
        out.append(capo_braket.types.job_event_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobEvents:
    import capo_braket.types.job_event_details

    out: JobEvents = []
    for item in data:
        out.append(capo_braket.types.job_event_details.deserialize_json(item))
    return out
