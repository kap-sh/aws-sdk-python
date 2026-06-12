"""Generated from Smithy shape ``com.amazonaws.cloudfront#VerifyDnsConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.dns_configuration_list


class VerifyDnsConfigurationResult(TypedDict):
    dns_configuration_list: NotRequired[
        "aws_sdk_cloudfront.types.dns_configuration_list.DnsConfigurationList"
    ]
    """<p>The list of domain names, their statuses, and a description of each status.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: VerifyDnsConfigurationResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "dns_configuration_list" in value:
        import aws_sdk_cloudfront.types.dns_configuration_list

        aws_sdk_cloudfront.types.dns_configuration_list.serialize_xml(
            value["dns_configuration_list"], el, "DnsConfigurationList"
        )


def deserialize_xml(el: Element) -> VerifyDnsConfigurationResult:
    out: VerifyDnsConfigurationResult = {}  # type: ignore[typeddict-item]
    child_dns_configuration_list = el.find("DnsConfigurationList")
    if child_dns_configuration_list is not None:
        import aws_sdk_cloudfront.types.dns_configuration_list

        out["dns_configuration_list"] = (
            aws_sdk_cloudfront.types.dns_configuration_list.deserialize_xml(
                child_dns_configuration_list
            )
        )
    return out
