"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayPolicyTableResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_policy_table


class CreateTransitGatewayPolicyTableResult(TypedDict):
    transit_gateway_policy_table: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table.TransitGatewayPolicyTable"
    ]
    """<p>Describes the created transit gateway policy table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayPolicyTableResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_policy_table" in value:
        import aws_sdk_ec2.types.transit_gateway_policy_table

        aws_sdk_ec2.types.transit_gateway_policy_table.serialize_ec2_query(
            value["transit_gateway_policy_table"],
            pairs,
            f"{prefix}.TransitGatewayPolicyTable",
        )


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayPolicyTableResult:
    out: CreateTransitGatewayPolicyTableResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_policy_table = el.find("TransitGatewayPolicyTable")
    if child_transit_gateway_policy_table is not None:
        import aws_sdk_ec2.types.transit_gateway_policy_table

        out["transit_gateway_policy_table"] = (
            aws_sdk_ec2.types.transit_gateway_policy_table.deserialize_ec2_query(
                child_transit_gateway_policy_table
            )
        )
    return out
