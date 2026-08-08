"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayPrefixListReferenceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_prefix_list_reference


class DeleteTransitGatewayPrefixListReferenceResult(TypedDict, closed=True):
    transit_gateway_prefix_list_reference: NotRequired[
        "capo_ec2.types.transit_gateway_prefix_list_reference.TransitGatewayPrefixListReference"
    ]
    """<p>Information about the deleted prefix list reference.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayPrefixListReferenceResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_prefix_list_reference" in value:
        import capo_ec2.types.transit_gateway_prefix_list_reference

        capo_ec2.types.transit_gateway_prefix_list_reference.serialize_ec2_query(
            value["transit_gateway_prefix_list_reference"],
            pairs,
            f"{key_prefix}TransitGatewayPrefixListReference",
        )


def deserialize_ec2_query(el: Element) -> DeleteTransitGatewayPrefixListReferenceResult:
    out: DeleteTransitGatewayPrefixListReferenceResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_prefix_list_reference = el.find(
        "transitGatewayPrefixListReference"
    )
    if child_transit_gateway_prefix_list_reference is not None:
        import capo_ec2.types.transit_gateway_prefix_list_reference

        out["transit_gateway_prefix_list_reference"] = (
            capo_ec2.types.transit_gateway_prefix_list_reference.deserialize_ec2_query(
                child_transit_gateway_prefix_list_reference
            )
        )
    return out
