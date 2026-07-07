"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayPolicyTableAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_policy_table_association_list


class GetTransitGatewayPolicyTableAssociationsResult(TypedDict, closed=True):
    associations: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table_association_list.TransitGatewayPolicyTableAssociationList"
    ]
    """<p>Returns details about the transit gateway policy table association.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetTransitGatewayPolicyTableAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "associations" in value:
        import aws_sdk_ec2.types.transit_gateway_policy_table_association_list

        aws_sdk_ec2.types.transit_gateway_policy_table_association_list.serialize_ec2_query(
            value["associations"], pairs, f"{prefix}.Associations"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> GetTransitGatewayPolicyTableAssociationsResult:
    out: GetTransitGatewayPolicyTableAssociationsResult = {}  # type: ignore[typeddict-item]
    if el.find("Associations") is not None:
        import aws_sdk_ec2.types.transit_gateway_policy_table_association_list

        out["associations"] = (
            aws_sdk_ec2.types.transit_gateway_policy_table_association_list.deserialize_ec2_query(
                el, "Associations"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
