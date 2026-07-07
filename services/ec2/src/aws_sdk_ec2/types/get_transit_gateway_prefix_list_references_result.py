"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayPrefixListReferencesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_prefix_list_reference_set


class GetTransitGatewayPrefixListReferencesResult(TypedDict, closed=True):
    transit_gateway_prefix_list_references: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_prefix_list_reference_set.TransitGatewayPrefixListReferenceSet"
    ]
    """<p>Information about the prefix list references.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetTransitGatewayPrefixListReferencesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_prefix_list_references" in value:
        import aws_sdk_ec2.types.transit_gateway_prefix_list_reference_set

        aws_sdk_ec2.types.transit_gateway_prefix_list_reference_set.serialize_ec2_query(
            value["transit_gateway_prefix_list_references"],
            pairs,
            f"{prefix}.TransitGatewayPrefixListReferenceSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetTransitGatewayPrefixListReferencesResult:
    out: GetTransitGatewayPrefixListReferencesResult = {}  # type: ignore[typeddict-item]
    if el.find("TransitGatewayPrefixListReferenceSet") is not None:
        import aws_sdk_ec2.types.transit_gateway_prefix_list_reference_set

        out["transit_gateway_prefix_list_references"] = (
            aws_sdk_ec2.types.transit_gateway_prefix_list_reference_set.deserialize_ec2_query(
                el, "TransitGatewayPrefixListReferenceSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
