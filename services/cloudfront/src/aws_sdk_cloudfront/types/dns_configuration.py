"""Generated from Smithy shape ``com.amazonaws.cloudfront#DnsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.dns_configuration_status
    import aws_sdk_cloudfront.types.string


class DnsConfiguration(TypedDict):
    domain: "aws_sdk_cloudfront.types.string.string"
    """<p>The domain name that you're verifying.</p>"""
    status: "aws_sdk_cloudfront.types.dns_configuration_status.DnsConfigurationStatus"
    """<p>The status of your domain name.</p> <ul> <li> <p> <code>valid-configuration</code>: The domain name is correctly configured and points to the correct routing endpoint of the connection group.</p> </li> <li> <p> <code>invalid-configuration</code>: There is either a missing DNS record or the DNS record exists but it's using an incorrect routing endpoint. Update the DNS record to point to the correct routing endpoint.</p> </li> <li> <p> <code>unknown-configuration</code>: CloudFront can't validate your DNS configuration. This status can appear if CloudFront can't verify the DNS record, or the DNS lookup request failed or timed out.</p> </li> </ul>"""
    reason: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Explains the status of the DNS configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DnsConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Domain").text = str(value["domain"])
    import aws_sdk_cloudfront.types.dns_configuration_status

    aws_sdk_cloudfront.types.dns_configuration_status.serialize_xml(
        value["status"], el, "Status"
    )
    if "reason" in value:
        SubElement(el, "Reason").text = str(value["reason"])


def deserialize_xml(el: Element) -> DnsConfiguration:
    out: DnsConfiguration = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    else:
        raise DeserializationError("DnsConfiguration.domain required")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_cloudfront.types.dns_configuration_status

        out["status"] = (
            aws_sdk_cloudfront.types.dns_configuration_status.deserialize_xml(
                child_status
            )
        )
    else:
        raise DeserializationError("DnsConfiguration.status required")
    child_reason = el.find("Reason")
    if child_reason is not None:
        out["reason"] = str(child_reason.text or "")
    return out
