"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListDeviceInstancesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_instances
    import aws_sdk_device_farm.types.pagination_token


class ListDeviceInstancesResult(TypedDict, closed=True):
    device_instances: NotRequired[
        "aws_sdk_device_farm.types.device_instances.DeviceInstances"
    ]
    """<p>An object that contains information about your device instances.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>An identifier that can be used in the next call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeviceInstancesResult) -> dict:
    out: dict = {}
    if "device_instances" in value:
        import aws_sdk_device_farm.types.device_instances

        out["deviceInstances"] = (
            aws_sdk_device_farm.types.device_instances.serialize_aws_json_1_1(
                value["device_instances"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeviceInstancesResult:
    out: ListDeviceInstancesResult = {}  # type: ignore[typeddict-item]
    if "deviceInstances" in data:
        import aws_sdk_device_farm.types.device_instances

        out["device_instances"] = (
            aws_sdk_device_farm.types.device_instances.deserialize_aws_json_1_1(
                data["deviceInstances"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
