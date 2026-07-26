"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayMeteringPolicyEntriesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_metering_policy_entry_list


class GetTransitGatewayMeteringPolicyEntriesResult(TypedDict, closed=True):
    transit_gateway_metering_policy_entries: NotRequired[
        "capo_ec2.types.transit_gateway_metering_policy_entry_list.TransitGatewayMeteringPolicyEntryList"
    ]
    """<p>Information about the transit gateway metering policy entries.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetTransitGatewayMeteringPolicyEntriesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_metering_policy_entries" in value:
        import capo_ec2.types.transit_gateway_metering_policy_entry_list

        capo_ec2.types.transit_gateway_metering_policy_entry_list.serialize_ec2_query(
            value["transit_gateway_metering_policy_entries"],
            pairs,
            f"{prefix}.TransitGatewayMeteringPolicyEntries",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetTransitGatewayMeteringPolicyEntriesResult:
    out: GetTransitGatewayMeteringPolicyEntriesResult = {}  # type: ignore[typeddict-item]
    if el.find("TransitGatewayMeteringPolicyEntries") is not None:
        import capo_ec2.types.transit_gateway_metering_policy_entry_list

        out["transit_gateway_metering_policy_entries"] = (
            capo_ec2.types.transit_gateway_metering_policy_entry_list.deserialize_ec2_query(
                el, "TransitGatewayMeteringPolicyEntries"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
