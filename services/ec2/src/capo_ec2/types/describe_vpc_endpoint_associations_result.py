"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.vpc_endpoint_association_set


class DescribeVpcEndpointAssociationsResult(TypedDict, closed=True):
    vpc_endpoint_associations: NotRequired[
        "capo_ec2.types.vpc_endpoint_association_set.VpcEndpointAssociationSet"
    ]
    """<p>Details of the endpoint associations.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The pagination token.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc_endpoint_associations" in value:
        import capo_ec2.types.vpc_endpoint_association_set

        capo_ec2.types.vpc_endpoint_association_set.serialize_ec2_query(
            value["vpc_endpoint_associations"],
            pairs,
            f"{key_prefix}VpcEndpointAssociationSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcEndpointAssociationsResult:
    out: DescribeVpcEndpointAssociationsResult = {}  # type: ignore[typeddict-item]
    if el.find("vpcEndpointAssociationSet") is not None:
        import capo_ec2.types.vpc_endpoint_association_set

        out["vpc_endpoint_associations"] = (
            capo_ec2.types.vpc_endpoint_association_set.deserialize_ec2_query(
                el, "vpcEndpointAssociationSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
