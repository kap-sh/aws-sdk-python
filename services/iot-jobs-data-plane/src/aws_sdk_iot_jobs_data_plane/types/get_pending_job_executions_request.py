"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#GetPendingJobExecutionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_jobs_data_plane.types.thing_name


class GetPendingJobExecutionsRequest(TypedDict):
    thing_name: "aws_sdk_iot_jobs_data_plane.types.thing_name.ThingName"
    """<p>The name of the thing that is executing the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPendingJobExecutionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPendingJobExecutionsRequest:
    out: GetPendingJobExecutionsRequest = {}  # type: ignore[typeddict-item]
    return out
