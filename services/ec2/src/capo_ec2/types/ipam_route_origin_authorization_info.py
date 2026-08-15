"""Generated from Smithy shape ``com.amazonaws.ec2#IpamRouteOriginAuthorizationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.string


class IpamRouteOriginAuthorizationInfo(TypedDict, closed=True):
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address prefix in CIDR notation authorized by the ROA.</p>"""
    asn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Autonomous System Number (ASN) authorized to originate the prefix.</p>"""
    max_length: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum prefix length that the ASN is authorized to announce.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamRouteOriginAuthorizationInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cidr" in value:
        pairs.append((f"{key_prefix}Cidr", str(value["cidr"])))
    if "asn" in value:
        pairs.append((f"{key_prefix}Asn", str(value["asn"])))
    if "max_length" in value:
        pairs.append((f"{key_prefix}MaxLength", str(value["max_length"])))


def deserialize_ec2_query(el: Element) -> IpamRouteOriginAuthorizationInfo:
    out: IpamRouteOriginAuthorizationInfo = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_asn = el.find("asn")
    if child_asn is not None:
        out["asn"] = str(child_asn.text or "")
    child_max_length = el.find("maxLength")
    if child_max_length is not None:
        out["max_length"] = int(child_max_length.text or "")
    return out
