"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayMeteringPolicyResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_metering_policy


class ModifyTransitGatewayMeteringPolicyResult(TypedDict):
    transit_gateway_metering_policy: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy.TransitGatewayMeteringPolicy"
    ]
    """<p>Information about the modified transit gateway metering policy.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTransitGatewayMeteringPolicyResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_metering_policy" in value:
        import aws_sdk_ec2.types.transit_gateway_metering_policy

        aws_sdk_ec2.types.transit_gateway_metering_policy.serialize_ec2_query(
            value["transit_gateway_metering_policy"],
            pairs,
            f"{prefix}.TransitGatewayMeteringPolicy",
        )


def deserialize_ec2_query(el: Element) -> ModifyTransitGatewayMeteringPolicyResult:
    out: ModifyTransitGatewayMeteringPolicyResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_metering_policy = el.find("TransitGatewayMeteringPolicy")
    if child_transit_gateway_metering_policy is not None:
        import aws_sdk_ec2.types.transit_gateway_metering_policy

        out["transit_gateway_metering_policy"] = (
            aws_sdk_ec2.types.transit_gateway_metering_policy.deserialize_ec2_query(
                child_transit_gateway_metering_policy
            )
        )
    return out
