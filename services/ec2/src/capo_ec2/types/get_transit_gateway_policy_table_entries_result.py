"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayPolicyTableEntriesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_policy_table_entry_list


class GetTransitGatewayPolicyTableEntriesResult(TypedDict, closed=True):
    transit_gateway_policy_table_entries: NotRequired[
        "capo_ec2.types.transit_gateway_policy_table_entry_list.TransitGatewayPolicyTableEntryList"
    ]
    """<p>The entries for the transit gateway policy table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetTransitGatewayPolicyTableEntriesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_policy_table_entries" in value:
        import capo_ec2.types.transit_gateway_policy_table_entry_list

        capo_ec2.types.transit_gateway_policy_table_entry_list.serialize_ec2_query(
            value["transit_gateway_policy_table_entries"],
            pairs,
            f"{prefix}.TransitGatewayPolicyTableEntries",
        )


def deserialize_ec2_query(el: Element) -> GetTransitGatewayPolicyTableEntriesResult:
    out: GetTransitGatewayPolicyTableEntriesResult = {}  # type: ignore[typeddict-item]
    if el.find("TransitGatewayPolicyTableEntries") is not None:
        import capo_ec2.types.transit_gateway_policy_table_entry_list

        out["transit_gateway_policy_table_entries"] = (
            capo_ec2.types.transit_gateway_policy_table_entry_list.deserialize_ec2_query(
                el, "TransitGatewayPolicyTableEntries"
            )
        )
    return out
