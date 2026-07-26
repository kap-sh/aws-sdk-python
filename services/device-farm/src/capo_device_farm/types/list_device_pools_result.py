"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListDevicePoolsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.device_pools
    import capo_device_farm.types.pagination_token


class ListDevicePoolsResult(TypedDict, closed=True):
    device_pools: NotRequired["capo_device_farm.types.device_pools.DevicePools"]
    """<p>Information about the device pools.</p>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDevicePoolsResult) -> dict:
    out: dict = {}
    if "device_pools" in value:
        import capo_device_farm.types.device_pools

        out["devicePools"] = capo_device_farm.types.device_pools.serialize_aws_json_1_1(
            value["device_pools"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDevicePoolsResult:
    out: ListDevicePoolsResult = {}  # type: ignore[typeddict-item]
    if "devicePools" in data:
        import capo_device_farm.types.device_pools

        out["device_pools"] = (
            capo_device_farm.types.device_pools.deserialize_aws_json_1_1(
                data["devicePools"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
