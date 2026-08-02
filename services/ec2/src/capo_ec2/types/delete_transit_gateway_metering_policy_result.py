"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayMeteringPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_metering_policy


class DeleteTransitGatewayMeteringPolicyResult(TypedDict, closed=True):
    transit_gateway_metering_policy: NotRequired[
        "capo_ec2.types.transit_gateway_metering_policy.TransitGatewayMeteringPolicy"
    ]
    """<p>Information about the deleted transit gateway metering policy.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayMeteringPolicyResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_metering_policy" in value:
        import capo_ec2.types.transit_gateway_metering_policy

        capo_ec2.types.transit_gateway_metering_policy.serialize_ec2_query(
            value["transit_gateway_metering_policy"],
            pairs,
            f"{key_prefix}TransitGatewayMeteringPolicy",
        )


def deserialize_ec2_query(el: Element) -> DeleteTransitGatewayMeteringPolicyResult:
    out: DeleteTransitGatewayMeteringPolicyResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_metering_policy = el.find("TransitGatewayMeteringPolicy")
    if child_transit_gateway_metering_policy is not None:
        import capo_ec2.types.transit_gateway_metering_policy

        out["transit_gateway_metering_policy"] = (
            capo_ec2.types.transit_gateway_metering_policy.deserialize_ec2_query(
                child_transit_gateway_metering_policy
            )
        )
    return out
