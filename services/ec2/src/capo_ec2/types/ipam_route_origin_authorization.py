"""Generated from Smithy shape ``com.amazonaws.ec2#IpamRouteOriginAuthorization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class IpamRouteOriginAuthorization(TypedDict, closed=True):
    asn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Autonomous System Number (ASN) authorized by the ROA.</p>"""
    prefix: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address prefix authorized by the ROA in CIDR notation.</p>"""
    max_length: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum prefix length that the ASN is authorized to announce.</p>"""
    match: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether the ROA matches the route announcement.</p>"""
    expiration: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The expiration date of the ROA.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamRouteOriginAuthorization, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "asn" in value:
        pairs.append((f"{key_prefix}Asn", str(value["asn"])))
    if "prefix" in value:
        pairs.append((f"{key_prefix}Prefix", str(value["prefix"])))
    if "max_length" in value:
        pairs.append((f"{key_prefix}MaxLength", str(value["max_length"])))
    if "match" in value:
        pairs.append((f"{key_prefix}Match", "true" if value["match"] else "false"))
    if "expiration" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["expiration"], pairs, f"{key_prefix}Expiration"
        )


def deserialize_ec2_query(el: Element) -> IpamRouteOriginAuthorization:
    out: IpamRouteOriginAuthorization = {}  # type: ignore[typeddict-item]
    child_asn = el.find("asn")
    if child_asn is not None:
        out["asn"] = str(child_asn.text or "")
    child_prefix = el.find("prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_max_length = el.find("maxLength")
    if child_max_length is not None:
        out["max_length"] = int(child_max_length.text or "")
    child_match = el.find("match")
    if child_match is not None:
        out["match"] = (child_match.text or "").lower() == "true"
    child_expiration = el.find("expiration")
    if child_expiration is not None:
        import capo_ec2.types.millisecond_date_time

        out["expiration"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_expiration
        )
    return out
