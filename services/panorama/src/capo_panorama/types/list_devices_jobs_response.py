"""Generated from Smithy shape ``com.amazonaws.panorama#ListDevicesJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.device_job_list
    import capo_panorama.types.next_token


class ListDevicesJobsResponse(TypedDict, closed=True):
    device_jobs: NotRequired["capo_panorama.types.device_job_list.DeviceJobList"]
    """<p>A list of jobs.</p>"""
    next_token: NotRequired["capo_panorama.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicesJobsResponse) -> dict:
    out: dict = {}
    if "device_jobs" in value:
        import capo_panorama.types.device_job_list

        out["DeviceJobs"] = capo_panorama.types.device_job_list.serialize_json(
            value["device_jobs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDevicesJobsResponse:
    out: ListDevicesJobsResponse = {}  # type: ignore[typeddict-item]
    if "DeviceJobs" in data:
        import capo_panorama.types.device_job_list

        out["device_jobs"] = capo_panorama.types.device_job_list.deserialize_json(
            data["DeviceJobs"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
