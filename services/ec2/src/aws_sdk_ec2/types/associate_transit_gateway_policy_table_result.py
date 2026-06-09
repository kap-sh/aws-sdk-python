"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateTransitGatewayPolicyTableResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_policy_table_association


class AssociateTransitGatewayPolicyTableResult(TypedDict):
    association: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table_association.TransitGatewayPolicyTableAssociation"
    ]
    """<p>Describes the association of a transit gateway and a transit gateway policy table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateTransitGatewayPolicyTableResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "association" in value:
        import aws_sdk_ec2.types.transit_gateway_policy_table_association

        aws_sdk_ec2.types.transit_gateway_policy_table_association.serialize_ec2_query(
            value["association"], pairs, f"{prefix}.Association"
        )


def deserialize_ec2_query(el: Element) -> AssociateTransitGatewayPolicyTableResult:
    out: AssociateTransitGatewayPolicyTableResult = {}  # type: ignore[typeddict-item]
    child_association = el.find("Association")
    if child_association is not None:
        import aws_sdk_ec2.types.transit_gateway_policy_table_association

        out["association"] = (
            aws_sdk_ec2.types.transit_gateway_policy_table_association.deserialize_ec2_query(
                child_association
            )
        )
    return out
