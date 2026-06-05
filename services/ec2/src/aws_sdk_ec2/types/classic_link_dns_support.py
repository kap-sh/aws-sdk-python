"""Generated from Smithy shape ``com.amazonaws.ec2#ClassicLinkDnsSupport``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class ClassicLinkDnsSupport(TypedDict):
    classic_link_dns_supported: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether ClassicLink DNS support is enabled for the VPC.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClassicLinkDnsSupport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "classic_link_dns_supported" in value:
        pairs.append(
            (
                f"{prefix}.ClassicLinkDnsSupported",
                "true" if value["classic_link_dns_supported"] else "false",
            )
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))


def deserialize_ec2_query(el: Element) -> ClassicLinkDnsSupport:
    out: ClassicLinkDnsSupport = {}  # type: ignore[typeddict-item]
    child_classic_link_dns_supported = el.find("ClassicLinkDnsSupported")
    if child_classic_link_dns_supported is not None:
        out["classic_link_dns_supported"] = (
            child_classic_link_dns_supported.text or ""
        ).lower() == "true"
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    return out
