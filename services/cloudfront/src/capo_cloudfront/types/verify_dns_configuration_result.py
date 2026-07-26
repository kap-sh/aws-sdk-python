"""Generated from Smithy shape ``com.amazonaws.cloudfront#VerifyDnsConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.dns_configuration_list


class VerifyDnsConfigurationResult(TypedDict, closed=True):
    dns_configuration_list: NotRequired[
        "capo_cloudfront.types.dns_configuration_list.DnsConfigurationList"
    ]
    """<p>The list of domain names, their statuses, and a description of each status.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: VerifyDnsConfigurationResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "dns_configuration_list" in value:
        import capo_cloudfront.types.dns_configuration_list

        capo_cloudfront.types.dns_configuration_list.serialize_xml(
            value["dns_configuration_list"], el, "DnsConfigurationList"
        )


def deserialize_xml(el: Element) -> VerifyDnsConfigurationResult:
    out: VerifyDnsConfigurationResult = {}  # type: ignore[typeddict-item]
    child_dns_configuration_list = el.find("DnsConfigurationList")
    if child_dns_configuration_list is not None:
        import capo_cloudfront.types.dns_configuration_list

        out["dns_configuration_list"] = (
            capo_cloudfront.types.dns_configuration_list.deserialize_xml(
                child_dns_configuration_list
            )
        )
    return out
