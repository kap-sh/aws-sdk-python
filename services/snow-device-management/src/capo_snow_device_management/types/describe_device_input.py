"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#DescribeDeviceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_snow_device_management.types.managed_device_id


class DescribeDeviceInput(TypedDict, closed=True):
    managed_device_id: (
        "capo_snow_device_management.types.managed_device_id.ManagedDeviceId"
    )
    """<p>The ID of the device that you are checking the information of.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDeviceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDeviceInput:
    out: DescribeDeviceInput = {}  # type: ignore[typeddict-item]
    return out
