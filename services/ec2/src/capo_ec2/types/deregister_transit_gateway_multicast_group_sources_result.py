"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterTransitGatewayMulticastGroupSourcesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_multicast_deregistered_group_sources


class DeregisterTransitGatewayMulticastGroupSourcesResult(TypedDict, closed=True):
    deregistered_multicast_group_sources: NotRequired[
        "capo_ec2.types.transit_gateway_multicast_deregistered_group_sources.TransitGatewayMulticastDeregisteredGroupSources"
    ]
    """<p>Information about the deregistered group sources.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeregisterTransitGatewayMulticastGroupSourcesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "deregistered_multicast_group_sources" in value:
        import capo_ec2.types.transit_gateway_multicast_deregistered_group_sources

        capo_ec2.types.transit_gateway_multicast_deregistered_group_sources.serialize_ec2_query(
            value["deregistered_multicast_group_sources"],
            pairs,
            f"{key_prefix}DeregisteredMulticastGroupSources",
        )


def deserialize_ec2_query(
    el: Element,
) -> DeregisterTransitGatewayMulticastGroupSourcesResult:
    out: DeregisterTransitGatewayMulticastGroupSourcesResult = {}  # type: ignore[typeddict-item]
    child_deregistered_multicast_group_sources = el.find(
        "deregisteredMulticastGroupSources"
    )
    if child_deregistered_multicast_group_sources is not None:
        import capo_ec2.types.transit_gateway_multicast_deregistered_group_sources

        out["deregistered_multicast_group_sources"] = (
            capo_ec2.types.transit_gateway_multicast_deregistered_group_sources.deserialize_ec2_query(
                child_deregistered_multicast_group_sources
            )
        )
    return out
