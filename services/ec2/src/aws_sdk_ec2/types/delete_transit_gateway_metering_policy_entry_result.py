"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayMeteringPolicyEntryResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_metering_policy_entry


class DeleteTransitGatewayMeteringPolicyEntryResult(TypedDict):
    transit_gateway_metering_policy_entry: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy_entry.TransitGatewayMeteringPolicyEntry"
    ]
    """<p>Information about the deleted transit gateway metering policy entry.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayMeteringPolicyEntryResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_metering_policy_entry" in value:
        import aws_sdk_ec2.types.transit_gateway_metering_policy_entry

        aws_sdk_ec2.types.transit_gateway_metering_policy_entry.serialize_ec2_query(
            value["transit_gateway_metering_policy_entry"],
            pairs,
            f"{prefix}.TransitGatewayMeteringPolicyEntry",
        )


def deserialize_ec2_query(el: Element) -> DeleteTransitGatewayMeteringPolicyEntryResult:
    out: DeleteTransitGatewayMeteringPolicyEntryResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_metering_policy_entry = el.find(
        "TransitGatewayMeteringPolicyEntry"
    )
    if child_transit_gateway_metering_policy_entry is not None:
        import aws_sdk_ec2.types.transit_gateway_metering_policy_entry

        out["transit_gateway_metering_policy_entry"] = (
            aws_sdk_ec2.types.transit_gateway_metering_policy_entry.deserialize_ec2_query(
                child_transit_gateway_metering_policy_entry
            )
        )
    return out
