"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateDevicePoolResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.device_pool


class CreateDevicePoolResult(TypedDict, closed=True):
    device_pool: NotRequired["capo_device_farm.types.device_pool.DevicePool"]
    """<p>The newly created device pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDevicePoolResult) -> dict:
    out: dict = {}
    if "device_pool" in value:
        import capo_device_farm.types.device_pool

        out["devicePool"] = capo_device_farm.types.device_pool.serialize_aws_json_1_1(
            value["device_pool"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDevicePoolResult:
    out: CreateDevicePoolResult = {}  # type: ignore[typeddict-item]
    if "devicePool" in data:
        import capo_device_farm.types.device_pool

        out["device_pool"] = (
            capo_device_farm.types.device_pool.deserialize_aws_json_1_1(
                data["devicePool"]
            )
        )
    return out
