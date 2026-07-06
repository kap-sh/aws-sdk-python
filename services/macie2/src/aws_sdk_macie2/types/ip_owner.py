"""Generated from Smithy shape ``com.amazonaws.macie2#IpOwner``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class IpOwner(TypedDict, closed=True):
    asn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The autonomous system number (ASN) for the autonomous system that included the IP address.</p>"""
    asn_org: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The organization identifier that's associated with the autonomous system number (ASN) for the autonomous system that included the IP address.</p>"""
    isp: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name of the internet service provider (ISP) that owned the IP address.</p>"""
    org: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name of the organization that owned the IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpOwner) -> dict:
    out: dict = {}
    if "asn" in value:
        out["asn"] = value["asn"]
    if "asn_org" in value:
        out["asnOrg"] = value["asn_org"]
    if "isp" in value:
        out["isp"] = value["isp"]
    if "org" in value:
        out["org"] = value["org"]
    return out


def deserialize_json(data: dict) -> IpOwner:
    out: IpOwner = {}  # type: ignore[typeddict-item]
    if "asn" in data:
        out["asn"] = data["asn"]
    if "asnOrg" in data:
        out["asn_org"] = data["asnOrg"]
    if "isp" in data:
        out["isp"] = data["isp"]
    if "org" in data:
        out["org"] = data["org"]
    return out
