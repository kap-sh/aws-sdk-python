"""Generated from Smithy shape ``com.amazonaws.codebuild#NetworkInterface``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string


class NetworkInterface(TypedDict):
    subnet_id: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the subnet.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the network interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkInterface) -> dict:
    out: dict = {}
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "network_interface_id" in value:
        out["networkInterfaceId"] = value["network_interface_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    if "subnetId" in data:
        out["subnet_id"] = data["subnetId"]
    if "networkInterfaceId" in data:
        out["network_interface_id"] = data["networkInterfaceId"]
    return out
