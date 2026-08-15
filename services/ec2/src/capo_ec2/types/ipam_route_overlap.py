"""Generated from Smithy shape ``com.amazonaws.ec2#IpamRouteOverlap``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class IpamRouteOverlap(TypedDict, closed=True):
    prefix: NotRequired["capo_ec2.types.string.String"]
    """<p>The overlapping IP address prefix in CIDR notation.</p>"""
    asn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ASN originating the overlapping route.</p>"""
    detected_at: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The time when the overlap was detected.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamRouteOverlap, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "prefix" in value:
        pairs.append((f"{key_prefix}Prefix", str(value["prefix"])))
    if "asn" in value:
        pairs.append((f"{key_prefix}Asn", str(value["asn"])))
    if "detected_at" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["detected_at"], pairs, f"{key_prefix}DetectedAt"
        )


def deserialize_ec2_query(el: Element) -> IpamRouteOverlap:
    out: IpamRouteOverlap = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_asn = el.find("asn")
    if child_asn is not None:
        out["asn"] = str(child_asn.text or "")
    child_detected_at = el.find("detectedAt")
    if child_detected_at is not None:
        import capo_ec2.types.millisecond_date_time

        out["detected_at"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_detected_at
        )
    return out
