"""Generated from Smithy shape ``com.amazonaws.storagegateway#EndpointNetworkConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.ip_address_list


class EndpointNetworkConfiguration(TypedDict):
    ip_addresses: NotRequired[
        "aws_sdk_storage_gateway.types.ip_address_list.IpAddressList"
    ]
    """<p>A list of gateway IP addresses on which the associated Amazon FSx file system is available.</p> <note> <p>If multiple file systems are associated with this gateway, this field is required.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointNetworkConfiguration) -> dict:
    out: dict = {}
    if "ip_addresses" in value:
        import aws_sdk_storage_gateway.types.ip_address_list

        out["IpAddresses"] = (
            aws_sdk_storage_gateway.types.ip_address_list.serialize_aws_json_1_1(
                value["ip_addresses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointNetworkConfiguration:
    out: EndpointNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if "IpAddresses" in data:
        import aws_sdk_storage_gateway.types.ip_address_list

        out["ip_addresses"] = (
            aws_sdk_storage_gateway.types.ip_address_list.deserialize_aws_json_1_1(
                data["IpAddresses"]
            )
        )
    return out
