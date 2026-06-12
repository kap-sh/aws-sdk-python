"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeVTLDevicesOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.marker
    import aws_sdk_storage_gateway.types.vtl_devices


class DescribeVTLDevicesOutput(TypedDict):
    gateway_arn: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]
    vtl_devices: NotRequired["aws_sdk_storage_gateway.types.vtl_devices.VTLDevices"]
    """<p>An array of VTL device objects composed of the Amazon Resource Name (ARN) of the VTL devices.</p>"""
    marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>An opaque string that indicates the position at which the VTL devices that were fetched for description ended. Use the marker in your next request to fetch the next set of VTL devices in the list. If there are no more VTL devices to describe, this field does not appear in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeVTLDevicesOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "vtl_devices" in value:
        import aws_sdk_storage_gateway.types.vtl_devices

        out["VTLDevices"] = (
            aws_sdk_storage_gateway.types.vtl_devices.serialize_aws_json_1_1(
                value["vtl_devices"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeVTLDevicesOutput:
    out: DescribeVTLDevicesOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "VTLDevices" in data:
        import aws_sdk_storage_gateway.types.vtl_devices

        out["vtl_devices"] = (
            aws_sdk_storage_gateway.types.vtl_devices.deserialize_aws_json_1_1(
                data["VTLDevices"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
