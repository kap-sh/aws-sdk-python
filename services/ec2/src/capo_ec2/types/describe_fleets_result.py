"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_set
    import capo_ec2.types.string


class DescribeFleetsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    fleets: NotRequired["capo_ec2.types.fleet_set.FleetSet"]
    """<p>Information about the EC2 Fleets.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFleetsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "fleets" in value:
        import capo_ec2.types.fleet_set

        capo_ec2.types.fleet_set.serialize_ec2_query(
            value["fleets"], pairs, f"{key_prefix}FleetSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeFleetsResult:
    out: DescribeFleetsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("fleetSet") is not None:
        import capo_ec2.types.fleet_set

        out["fleets"] = capo_ec2.types.fleet_set.deserialize_ec2_query(el, "fleetSet")
    return out
