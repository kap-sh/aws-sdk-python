"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeHostReservationOfferingsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.host_offering_set
    import capo_ec2.types.string


class DescribeHostReservationOfferingsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    offering_set: NotRequired["capo_ec2.types.host_offering_set.HostOfferingSet"]
    """<p>Information about the offerings.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeHostReservationOfferingsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "offering_set" in value:
        import capo_ec2.types.host_offering_set

        capo_ec2.types.host_offering_set.serialize_ec2_query(
            value["offering_set"], pairs, f"{key_prefix}OfferingSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeHostReservationOfferingsResult:
    out: DescribeHostReservationOfferingsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("OfferingSet") is not None:
        import capo_ec2.types.host_offering_set

        out["offering_set"] = capo_ec2.types.host_offering_set.deserialize_ec2_query(
            el, "OfferingSet"
        )
    return out
