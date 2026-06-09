"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_endpoint_association_set


class DescribeVpcEndpointAssociationsResult(TypedDict):
    vpc_endpoint_associations: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_association_set.VpcEndpointAssociationSet"
    ]
    """<p>Details of the endpoint associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The pagination token.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "vpc_endpoint_associations" in value:
        import aws_sdk_ec2.types.vpc_endpoint_association_set

        aws_sdk_ec2.types.vpc_endpoint_association_set.serialize_ec2_query(
            value["vpc_endpoint_associations"],
            pairs,
            f"{prefix}.VpcEndpointAssociationSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcEndpointAssociationsResult:
    out: DescribeVpcEndpointAssociationsResult = {}  # type: ignore[typeddict-item]
    if el.find("VpcEndpointAssociationSet") is not None:
        import aws_sdk_ec2.types.vpc_endpoint_association_set

        out["vpc_endpoint_associations"] = (
            aws_sdk_ec2.types.vpc_endpoint_association_set.deserialize_ec2_query(
                el, "VpcEndpointAssociationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
