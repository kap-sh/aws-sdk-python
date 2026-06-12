"""Generated from Smithy shape ``com.amazonaws.cloudfront#IpamConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.ipam_cidr_config_list


class IpamConfig(TypedDict):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of IPAM CIDR configurations in the <code>IpamCidrConfigs</code> list.</p>"""
    ipam_cidr_configs: (
        "aws_sdk_cloudfront.types.ipam_cidr_config_list.IpamCidrConfigList"
    )
    """<p>A list of IPAM CIDR configurations that define the IP address ranges, IPAM pools, and associated Anycast IP addresses.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: IpamConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    import aws_sdk_cloudfront.types.ipam_cidr_config_list

    aws_sdk_cloudfront.types.ipam_cidr_config_list.serialize_xml(
        value["ipam_cidr_configs"], el, "IpamCidrConfigs"
    )


def deserialize_xml(el: Element) -> IpamConfig:
    out: IpamConfig = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("IpamConfig.quantity required")
    child_ipam_cidr_configs = el.find("IpamCidrConfigs")
    if child_ipam_cidr_configs is not None:
        import aws_sdk_cloudfront.types.ipam_cidr_config_list

        out["ipam_cidr_configs"] = (
            aws_sdk_cloudfront.types.ipam_cidr_config_list.deserialize_xml(
                child_ipam_cidr_configs
            )
        )
    else:
        raise DeserializationError("IpamConfig.ipam_cidr_configs required")
    return out
