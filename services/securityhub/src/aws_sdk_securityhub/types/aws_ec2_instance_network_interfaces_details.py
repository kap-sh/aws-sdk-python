"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2InstanceNetworkInterfacesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2InstanceNetworkInterfacesDetails(TypedDict, closed=True):
    network_interface_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the network interface. The details are in a corresponding <code>AwsEc2NetworkInterfacesDetails</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2InstanceNetworkInterfacesDetails) -> dict:
    out: dict = {}
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    return out


def deserialize_json(data: dict) -> AwsEc2InstanceNetworkInterfacesDetails:
    out: AwsEc2InstanceNetworkInterfacesDetails = {}  # type: ignore[typeddict-item]
    if "NetworkInterfaceId" in data:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    return out
