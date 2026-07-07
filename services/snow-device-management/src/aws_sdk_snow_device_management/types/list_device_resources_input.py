"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ListDeviceResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.managed_device_id
    import aws_sdk_snow_device_management.types.max_results
    import aws_sdk_snow_device_management.types.next_token


class ListDeviceResourcesInput(TypedDict, closed=True):
    managed_device_id: (
        "aws_sdk_snow_device_management.types.managed_device_id.ManagedDeviceId"
    )
    """<p>The ID of the managed device that you are listing the resources of.</p>"""
    type: NotRequired["str"]
    """<p>A structure used to filter the results by type of resource.</p>"""
    max_results: NotRequired[
        "aws_sdk_snow_device_management.types.max_results.MaxResults"
    ]
    """<p>The maximum number of resources per page.</p>"""
    next_token: NotRequired["aws_sdk_snow_device_management.types.next_token.NextToken"]
    """<p>A pagination token to continue to the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeviceResourcesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDeviceResourcesInput:
    out: ListDeviceResourcesInput = {}  # type: ignore[typeddict-item]
    return out
