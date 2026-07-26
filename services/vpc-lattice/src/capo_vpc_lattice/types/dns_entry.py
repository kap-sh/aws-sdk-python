"""Generated from Smithy shape ``com.amazonaws.vpclattice#DnsEntry``."""

from typing_extensions import NotRequired, TypedDict


class DnsEntry(TypedDict, closed=True):
    domain_name: NotRequired["str"]
    """<p>The domain name of the service.</p>"""
    hosted_zone_id: NotRequired["str"]
    """<p>The ID of the hosted zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DnsEntry) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "hosted_zone_id" in value:
        out["hostedZoneId"] = value["hosted_zone_id"]
    return out


def deserialize_json(data: dict) -> DnsEntry:
    out: DnsEntry = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "hostedZoneId" in data:
        out["hosted_zone_id"] = data["hostedZoneId"]
    return out
