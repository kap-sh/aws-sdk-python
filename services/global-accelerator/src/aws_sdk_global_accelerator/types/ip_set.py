"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#IpSet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string
    import aws_sdk_global_accelerator.types.ip_address_family
    import aws_sdk_global_accelerator.types.ip_addresses


class IpSet(TypedDict):
    ip_family: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>IpFamily is deprecated and has been replaced by IpAddressFamily.</p>"""
    ip_addresses: NotRequired[
        "aws_sdk_global_accelerator.types.ip_addresses.IpAddresses"
    ]
    """<p>The array of IP addresses in the IP address set. An IP address set can have a maximum of two IP addresses.</p>"""
    ip_address_family: NotRequired[
        "aws_sdk_global_accelerator.types.ip_address_family.IpAddressFamily"
    ]
    """<p>The types of IP addresses included in this IP set. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpSet) -> dict:
    out: dict = {}
    if "ip_family" in value:
        out["IpFamily"] = value["ip_family"]
    if "ip_addresses" in value:
        import aws_sdk_global_accelerator.types.ip_addresses

        out["IpAddresses"] = (
            aws_sdk_global_accelerator.types.ip_addresses.serialize_aws_json_1_1(
                value["ip_addresses"]
            )
        )
    if "ip_address_family" in value:
        import aws_sdk_global_accelerator.types.ip_address_family

        out["IpAddressFamily"] = (
            aws_sdk_global_accelerator.types.ip_address_family.serialize_aws_json_1_1(
                value["ip_address_family"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IpSet:
    out: IpSet = {}  # type: ignore[typeddict-item]
    if "IpFamily" in data:
        out["ip_family"] = data["IpFamily"]
    if "IpAddresses" in data:
        import aws_sdk_global_accelerator.types.ip_addresses

        out["ip_addresses"] = (
            aws_sdk_global_accelerator.types.ip_addresses.deserialize_aws_json_1_1(
                data["IpAddresses"]
            )
        )
    if "IpAddressFamily" in data:
        import aws_sdk_global_accelerator.types.ip_address_family

        out["ip_address_family"] = (
            aws_sdk_global_accelerator.types.ip_address_family.deserialize_aws_json_1_1(
                data["IpAddressFamily"]
            )
        )
    return out
