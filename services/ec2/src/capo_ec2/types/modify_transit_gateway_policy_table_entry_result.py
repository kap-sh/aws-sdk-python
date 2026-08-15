"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayPolicyTableEntryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_policy_table_entry


class ModifyTransitGatewayPolicyTableEntryResult(TypedDict, closed=True):
    transit_gateway_policy_table_entry: NotRequired[
        "capo_ec2.types.transit_gateway_policy_table_entry.TransitGatewayPolicyTableEntry"
    ]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTransitGatewayPolicyTableEntryResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_policy_table_entry" in value:
        import capo_ec2.types.transit_gateway_policy_table_entry

        capo_ec2.types.transit_gateway_policy_table_entry.serialize_ec2_query(
            value["transit_gateway_policy_table_entry"],
            pairs,
            f"{key_prefix}TransitGatewayPolicyTableEntry",
        )


def deserialize_ec2_query(el: Element) -> ModifyTransitGatewayPolicyTableEntryResult:
    out: ModifyTransitGatewayPolicyTableEntryResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_policy_table_entry = el.find("transitGatewayPolicyTableEntry")
    if child_transit_gateway_policy_table_entry is not None:
        import capo_ec2.types.transit_gateway_policy_table_entry

        out["transit_gateway_policy_table_entry"] = (
            capo_ec2.types.transit_gateway_policy_table_entry.deserialize_ec2_query(
                child_transit_gateway_policy_table_entry
            )
        )
    return out
