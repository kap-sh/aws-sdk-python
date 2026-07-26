"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayAttachmentPropagationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_attachment_propagation_list


class GetTransitGatewayAttachmentPropagationsResult(TypedDict, closed=True):
    transit_gateway_attachment_propagations: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_propagation_list.TransitGatewayAttachmentPropagationList"
    ]
    """<p>Information about the propagation route tables.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetTransitGatewayAttachmentPropagationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_attachment_propagations" in value:
        import capo_ec2.types.transit_gateway_attachment_propagation_list

        capo_ec2.types.transit_gateway_attachment_propagation_list.serialize_ec2_query(
            value["transit_gateway_attachment_propagations"],
            pairs,
            f"{prefix}.TransitGatewayAttachmentPropagations",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetTransitGatewayAttachmentPropagationsResult:
    out: GetTransitGatewayAttachmentPropagationsResult = {}  # type: ignore[typeddict-item]
    if el.find("TransitGatewayAttachmentPropagations") is not None:
        import capo_ec2.types.transit_gateway_attachment_propagation_list

        out["transit_gateway_attachment_propagations"] = (
            capo_ec2.types.transit_gateway_attachment_propagation_list.deserialize_ec2_query(
                el, "TransitGatewayAttachmentPropagations"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
