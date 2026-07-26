"""Generated from Smithy shape ``com.amazonaws.storagegateway#EndpointNetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.ip_address_list


class EndpointNetworkConfiguration(TypedDict, closed=True):
    ip_addresses: NotRequired[
        "capo_storage_gateway.types.ip_address_list.IpAddressList"
    ]
    """<p>A list of gateway IP addresses on which the associated Amazon FSx file system is available.</p> <note> <p>If multiple file systems are associated with this gateway, this field is required.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointNetworkConfiguration) -> dict:
    out: dict = {}
    if "ip_addresses" in value:
        import capo_storage_gateway.types.ip_address_list

        out["IpAddresses"] = (
            capo_storage_gateway.types.ip_address_list.serialize_aws_json_1_1(
                value["ip_addresses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointNetworkConfiguration:
    out: EndpointNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if "IpAddresses" in data:
        import capo_storage_gateway.types.ip_address_list

        out["ip_addresses"] = (
            capo_storage_gateway.types.ip_address_list.deserialize_aws_json_1_1(
                data["IpAddresses"]
            )
        )
    return out
