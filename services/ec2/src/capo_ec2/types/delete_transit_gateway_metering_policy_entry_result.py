"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayMeteringPolicyEntryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_metering_policy_entry


class DeleteTransitGatewayMeteringPolicyEntryResult(TypedDict, closed=True):
    transit_gateway_metering_policy_entry: NotRequired[
        "capo_ec2.types.transit_gateway_metering_policy_entry.TransitGatewayMeteringPolicyEntry"
    ]
    """<p>Information about the deleted transit gateway metering policy entry.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayMeteringPolicyEntryResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_metering_policy_entry" in value:
        import capo_ec2.types.transit_gateway_metering_policy_entry

        capo_ec2.types.transit_gateway_metering_policy_entry.serialize_ec2_query(
            value["transit_gateway_metering_policy_entry"],
            pairs,
            f"{key_prefix}TransitGatewayMeteringPolicyEntry",
        )


def deserialize_ec2_query(el: Element) -> DeleteTransitGatewayMeteringPolicyEntryResult:
    out: DeleteTransitGatewayMeteringPolicyEntryResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_metering_policy_entry = el.find(
        "transitGatewayMeteringPolicyEntry"
    )
    if child_transit_gateway_metering_policy_entry is not None:
        import capo_ec2.types.transit_gateway_metering_policy_entry

        out["transit_gateway_metering_policy_entry"] = (
            capo_ec2.types.transit_gateway_metering_policy_entry.deserialize_ec2_query(
                child_transit_gateway_metering_policy_entry
            )
        )
    return out
