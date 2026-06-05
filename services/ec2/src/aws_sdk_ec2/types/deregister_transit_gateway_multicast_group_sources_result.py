"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterTransitGatewayMulticastGroupSourcesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_multicast_deregistered_group_sources


class DeregisterTransitGatewayMulticastGroupSourcesResult(TypedDict):
    deregistered_multicast_group_sources: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_deregistered_group_sources.TransitGatewayMulticastDeregisteredGroupSources"
    ]
    """<p>Information about the deregistered group sources.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeregisterTransitGatewayMulticastGroupSourcesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "deregistered_multicast_group_sources" in value:
        import aws_sdk_ec2.types.transit_gateway_multicast_deregistered_group_sources

        aws_sdk_ec2.types.transit_gateway_multicast_deregistered_group_sources.serialize_ec2_query(
            value["deregistered_multicast_group_sources"],
            pairs,
            f"{prefix}.DeregisteredMulticastGroupSources",
        )


def deserialize_ec2_query(
    el: Element,
) -> DeregisterTransitGatewayMulticastGroupSourcesResult:
    out: DeregisterTransitGatewayMulticastGroupSourcesResult = {}  # type: ignore[typeddict-item]
    child_deregistered_multicast_group_sources = el.find(
        "DeregisteredMulticastGroupSources"
    )
    if child_deregistered_multicast_group_sources is not None:
        import aws_sdk_ec2.types.transit_gateway_multicast_deregistered_group_sources

        out["deregistered_multicast_group_sources"] = (
            aws_sdk_ec2.types.transit_gateway_multicast_deregistered_group_sources.deserialize_ec2_query(
                child_deregistered_multicast_group_sources
            )
        )
    return out
