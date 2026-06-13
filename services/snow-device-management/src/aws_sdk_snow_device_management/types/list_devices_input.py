"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ListDevicesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.job_id
    import aws_sdk_snow_device_management.types.max_results
    import aws_sdk_snow_device_management.types.next_token


class ListDevicesInput(TypedDict):
    job_id: NotRequired["aws_sdk_snow_device_management.types.job_id.JobId"]
    """<p>The ID of the job used to order the device.</p>"""
    max_results: NotRequired[
        "aws_sdk_snow_device_management.types.max_results.MaxResults"
    ]
    """<p>The maximum number of devices to list per page.</p>"""
    next_token: NotRequired["aws_sdk_snow_device_management.types.next_token.NextToken"]
    """<p>A pagination token to continue to the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDevicesInput:
    out: ListDevicesInput = {}  # type: ignore[typeddict-item]
    return out
