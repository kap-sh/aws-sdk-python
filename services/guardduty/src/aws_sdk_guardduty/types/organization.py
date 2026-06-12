"""Generated from Smithy shape ``com.amazonaws.guardduty#Organization``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class Organization(TypedDict):
    asn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Autonomous System Number (ASN) of the internet provider of the remote IP address.</p>"""
    asn_org: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The organization that registered this ASN.</p>"""
    isp: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ISP information for the internet provider.</p>"""
    org: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the internet provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Organization) -> dict:
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


def deserialize_json(data: dict) -> Organization:
    out: Organization = {}  # type: ignore[typeddict-item]
    if "asn" in data:
        out["asn"] = data["asn"]
    if "asnOrg" in data:
        out["asn_org"] = data["asnOrg"]
    if "isp" in data:
        out["isp"] = data["isp"]
    if "org" in data:
        out["org"] = data["org"]
    return out
