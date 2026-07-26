"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayMeteringPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_metering_policy


class CreateTransitGatewayMeteringPolicyResult(TypedDict, closed=True):
    transit_gateway_metering_policy: NotRequired[
        "capo_ec2.types.transit_gateway_metering_policy.TransitGatewayMeteringPolicy"
    ]
    """<p>Information about the created transit gateway metering policy.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayMeteringPolicyResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_metering_policy" in value:
        import capo_ec2.types.transit_gateway_metering_policy

        capo_ec2.types.transit_gateway_metering_policy.serialize_ec2_query(
            value["transit_gateway_metering_policy"],
            pairs,
            f"{prefix}.TransitGatewayMeteringPolicy",
        )


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayMeteringPolicyResult:
    out: CreateTransitGatewayMeteringPolicyResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_metering_policy = el.find("TransitGatewayMeteringPolicy")
    if child_transit_gateway_metering_policy is not None:
        import capo_ec2.types.transit_gateway_metering_policy

        out["transit_gateway_metering_policy"] = (
            capo_ec2.types.transit_gateway_metering_policy.deserialize_ec2_query(
                child_transit_gateway_metering_policy
            )
        )
    return out
