"""Generated from Smithy shape ``com.amazonaws.groundstation#DiscoveryData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.capability_arn_list
    import capo_groundstation.types.ip_address_list


class DiscoveryData(TypedDict, closed=True):
    public_ip_addresses: "capo_groundstation.types.ip_address_list.IpAddressList"
    """<p>List of public IP addresses to associate with agent.</p>"""
    private_ip_addresses: "capo_groundstation.types.ip_address_list.IpAddressList"
    """<p>List of private IP addresses to associate with agent.</p>"""
    capability_arns: "capo_groundstation.types.capability_arn_list.CapabilityArnList"
    """<p>List of capabilities to associate with agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveryData) -> dict:
    out: dict = {}
    import capo_groundstation.types.ip_address_list

    out["publicIpAddresses"] = capo_groundstation.types.ip_address_list.serialize_json(
        value["public_ip_addresses"]
    )
    import capo_groundstation.types.ip_address_list

    out["privateIpAddresses"] = capo_groundstation.types.ip_address_list.serialize_json(
        value["private_ip_addresses"]
    )
    import capo_groundstation.types.capability_arn_list

    out["capabilityArns"] = capo_groundstation.types.capability_arn_list.serialize_json(
        value["capability_arns"]
    )
    return out


def deserialize_json(data: dict) -> DiscoveryData:
    out: DiscoveryData = {}  # type: ignore[typeddict-item]
    if "publicIpAddresses" in data:
        import capo_groundstation.types.ip_address_list

        out["public_ip_addresses"] = (
            capo_groundstation.types.ip_address_list.deserialize_json(
                data["publicIpAddresses"]
            )
        )
    else:
        raise DeserializationError("DiscoveryData.public_ip_addresses required")
    if "privateIpAddresses" in data:
        import capo_groundstation.types.ip_address_list

        out["private_ip_addresses"] = (
            capo_groundstation.types.ip_address_list.deserialize_json(
                data["privateIpAddresses"]
            )
        )
    else:
        raise DeserializationError("DiscoveryData.private_ip_addresses required")
    if "capabilityArns" in data:
        import capo_groundstation.types.capability_arn_list

        out["capability_arns"] = (
            capo_groundstation.types.capability_arn_list.deserialize_json(
                data["capabilityArns"]
            )
        )
    else:
        raise DeserializationError("DiscoveryData.capability_arns required")
    return out
