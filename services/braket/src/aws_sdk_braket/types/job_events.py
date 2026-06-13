"""Generated from Smithy shape ``com.amazonaws.braket#JobEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_braket.types.job_event_details

JobEvents: TypeAlias = list["aws_sdk_braket.types.job_event_details.JobEventDetails"]


# --- restJson1 ser/de ---
def serialize_json(value: JobEvents) -> list:
    import aws_sdk_braket.types.job_event_details

    out: list = []
    for item in value:
        out.append(aws_sdk_braket.types.job_event_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobEvents:
    import aws_sdk_braket.types.job_event_details

    out: JobEvents = []
    for item in data:
        out.append(aws_sdk_braket.types.job_event_details.deserialize_json(item))
    return out
