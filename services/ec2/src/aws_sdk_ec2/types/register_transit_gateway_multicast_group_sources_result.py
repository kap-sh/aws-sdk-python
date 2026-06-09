"""Generated from Smithy shape ``com.amazonaws.ec2#RegisterTransitGatewayMulticastGroupSourcesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_multicast_registered_group_sources


class RegisterTransitGatewayMulticastGroupSourcesResult(TypedDict):
    registered_multicast_group_sources: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_registered_group_sources.TransitGatewayMulticastRegisteredGroupSources"
    ]
    """<p>Information about the transit gateway multicast group sources.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RegisterTransitGatewayMulticastGroupSourcesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "registered_multicast_group_sources" in value:
        import aws_sdk_ec2.types.transit_gateway_multicast_registered_group_sources

        aws_sdk_ec2.types.transit_gateway_multicast_registered_group_sources.serialize_ec2_query(
            value["registered_multicast_group_sources"],
            pairs,
            f"{prefix}.RegisteredMulticastGroupSources",
        )


def deserialize_ec2_query(
    el: Element,
) -> RegisterTransitGatewayMulticastGroupSourcesResult:
    out: RegisterTransitGatewayMulticastGroupSourcesResult = {}  # type: ignore[typeddict-item]
    child_registered_multicast_group_sources = el.find(
        "RegisteredMulticastGroupSources"
    )
    if child_registered_multicast_group_sources is not None:
        import aws_sdk_ec2.types.transit_gateway_multicast_registered_group_sources

        out["registered_multicast_group_sources"] = (
            aws_sdk_ec2.types.transit_gateway_multicast_registered_group_sources.deserialize_ec2_query(
                child_registered_multicast_group_sources
            )
        )
    return out
