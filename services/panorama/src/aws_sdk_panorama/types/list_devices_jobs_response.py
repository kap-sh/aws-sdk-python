"""Generated from Smithy shape ``com.amazonaws.panorama#ListDevicesJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_panorama.types.device_job_list
    import aws_sdk_panorama.types.next_token


class ListDevicesJobsResponse(TypedDict):
    device_jobs: NotRequired["aws_sdk_panorama.types.device_job_list.DeviceJobList"]
    """<p>A list of jobs.</p>"""
    next_token: NotRequired["aws_sdk_panorama.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicesJobsResponse) -> dict:
    out: dict = {}
    if "device_jobs" in value:
        import aws_sdk_panorama.types.device_job_list

        out["DeviceJobs"] = aws_sdk_panorama.types.device_job_list.serialize_json(
            value["device_jobs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDevicesJobsResponse:
    out: ListDevicesJobsResponse = {}  # type: ignore[typeddict-item]
    if "DeviceJobs" in data:
        import aws_sdk_panorama.types.device_job_list

        out["device_jobs"] = aws_sdk_panorama.types.device_job_list.deserialize_json(
            data["DeviceJobs"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
