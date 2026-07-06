"""Generated from Smithy shape ``com.amazonaws.quicksight#NetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.network_interface_id
    import aws_sdk_quicksight.types.network_interface_status
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.subnet_id


class NetworkInterface(TypedDict, closed=True):
    subnet_id: NotRequired["aws_sdk_quicksight.types.subnet_id.SubnetId"]
    """<p>The subnet ID associated with the network interface.</p>"""
    availability_zone: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The availability zone that the network interface resides in.</p>"""
    error_message: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>An error message.</p>"""
    status: NotRequired[
        "aws_sdk_quicksight.types.network_interface_status.NetworkInterfaceStatus"
    ]
    """<p>The status of the network interface.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_quicksight.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The network interface ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterface) -> dict:
    out: dict = {}
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "status" in value:
        import aws_sdk_quicksight.types.network_interface_status

        out["Status"] = (
            aws_sdk_quicksight.types.network_interface_status.serialize_json(
                value["status"]
            )
        )
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    return out


def deserialize_json(data: dict) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "Status" in data:
        import aws_sdk_quicksight.types.network_interface_status

        out["status"] = (
            aws_sdk_quicksight.types.network_interface_status.deserialize_json(
                data["Status"]
            )
        )
    if "NetworkInterfaceId" in data:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    return out
