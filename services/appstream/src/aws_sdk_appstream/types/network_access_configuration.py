"""Generated from Smithy shape ``com.amazonaws.appstream#NetworkAccessConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.string_list


class NetworkAccessConfiguration(TypedDict):
    eni_private_ip_address: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The private IP address of the elastic network interface that is attached to instances in your VPC.</p>"""
    eni_ipv6_addresses: NotRequired["aws_sdk_appstream.types.string_list.StringList"]
    """<p>The IPv6 addresses assigned to the elastic network interface. This field supports IPv6 connectivity for WorkSpaces Applications instances.</p>"""
    eni_id: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The resource identifier of the elastic network interface that is attached to instances in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkAccessConfiguration) -> dict:
    out: dict = {}
    if "eni_private_ip_address" in value:
        out["EniPrivateIpAddress"] = value["eni_private_ip_address"]
    if "eni_ipv6_addresses" in value:
        import aws_sdk_appstream.types.string_list

        out["EniIpv6Addresses"] = (
            aws_sdk_appstream.types.string_list.serialize_aws_json_1_1(
                value["eni_ipv6_addresses"]
            )
        )
    if "eni_id" in value:
        out["EniId"] = value["eni_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkAccessConfiguration:
    out: NetworkAccessConfiguration = {}  # type: ignore[typeddict-item]
    if "EniPrivateIpAddress" in data:
        out["eni_private_ip_address"] = data["EniPrivateIpAddress"]
    if "EniIpv6Addresses" in data:
        import aws_sdk_appstream.types.string_list

        out["eni_ipv6_addresses"] = (
            aws_sdk_appstream.types.string_list.deserialize_aws_json_1_1(
                data["EniIpv6Addresses"]
            )
        )
    if "EniId" in data:
        out["eni_id"] = data["EniId"]
    return out
