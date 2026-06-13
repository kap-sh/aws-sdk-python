"""Generated from Smithy shape ``com.amazonaws.groundstation#DiscoveryData``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.capability_arn_list
    import aws_sdk_groundstation.types.ip_address_list


class DiscoveryData(TypedDict):
    public_ip_addresses: "aws_sdk_groundstation.types.ip_address_list.IpAddressList"
    """<p>List of public IP addresses to associate with agent.</p>"""
    private_ip_addresses: "aws_sdk_groundstation.types.ip_address_list.IpAddressList"
    """<p>List of private IP addresses to associate with agent.</p>"""
    capability_arns: "aws_sdk_groundstation.types.capability_arn_list.CapabilityArnList"
    """<p>List of capabilities to associate with agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveryData) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.ip_address_list

    out["publicIpAddresses"] = (
        aws_sdk_groundstation.types.ip_address_list.serialize_json(
            value["public_ip_addresses"]
        )
    )
    import aws_sdk_groundstation.types.ip_address_list

    out["privateIpAddresses"] = (
        aws_sdk_groundstation.types.ip_address_list.serialize_json(
            value["private_ip_addresses"]
        )
    )
    import aws_sdk_groundstation.types.capability_arn_list

    out["capabilityArns"] = (
        aws_sdk_groundstation.types.capability_arn_list.serialize_json(
            value["capability_arns"]
        )
    )
    return out


def deserialize_json(data: dict) -> DiscoveryData:
    out: DiscoveryData = {}  # type: ignore[typeddict-item]
    if "publicIpAddresses" in data:
        import aws_sdk_groundstation.types.ip_address_list

        out["public_ip_addresses"] = (
            aws_sdk_groundstation.types.ip_address_list.deserialize_json(
                data["publicIpAddresses"]
            )
        )
    else:
        raise DeserializationError("DiscoveryData.public_ip_addresses required")
    if "privateIpAddresses" in data:
        import aws_sdk_groundstation.types.ip_address_list

        out["private_ip_addresses"] = (
            aws_sdk_groundstation.types.ip_address_list.deserialize_json(
                data["privateIpAddresses"]
            )
        )
    else:
        raise DeserializationError("DiscoveryData.private_ip_addresses required")
    if "capabilityArns" in data:
        import aws_sdk_groundstation.types.capability_arn_list

        out["capability_arns"] = (
            aws_sdk_groundstation.types.capability_arn_list.deserialize_json(
                data["capabilityArns"]
            )
        )
    else:
        raise DeserializationError("DiscoveryData.capability_arns required")
    return out
