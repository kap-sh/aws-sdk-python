"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastDomainOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.auto_accept_shared_associations_value
    import aws_sdk_ec2.types.igmpv2_support_value
    import aws_sdk_ec2.types.static_sources_support_value


class TransitGatewayMulticastDomainOptions(TypedDict):
    igmpv2_support: NotRequired[
        "aws_sdk_ec2.types.igmpv2_support_value.Igmpv2SupportValue"
    ]
    """<p>Indicates whether Internet Group Management Protocol (IGMP) version 2 is turned on for the transit gateway multicast domain.</p>"""
    static_sources_support: NotRequired[
        "aws_sdk_ec2.types.static_sources_support_value.StaticSourcesSupportValue"
    ]
    """<p>Indicates whether support for statically configuring transit gateway multicast group sources is turned on.</p>"""
    auto_accept_shared_associations: NotRequired[
        "aws_sdk_ec2.types.auto_accept_shared_associations_value.AutoAcceptSharedAssociationsValue"
    ]
    """<p>Indicates whether to automatically cross-account subnet associations that are associated with the transit gateway multicast domain.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMulticastDomainOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "igmpv2_support" in value:
        import aws_sdk_ec2.types.igmpv2_support_value

        aws_sdk_ec2.types.igmpv2_support_value.serialize_ec2_query(
            value["igmpv2_support"], pairs, f"{prefix}.Igmpv2Support"
        )
    if "static_sources_support" in value:
        import aws_sdk_ec2.types.static_sources_support_value

        aws_sdk_ec2.types.static_sources_support_value.serialize_ec2_query(
            value["static_sources_support"], pairs, f"{prefix}.StaticSourcesSupport"
        )
    if "auto_accept_shared_associations" in value:
        import aws_sdk_ec2.types.auto_accept_shared_associations_value

        aws_sdk_ec2.types.auto_accept_shared_associations_value.serialize_ec2_query(
            value["auto_accept_shared_associations"],
            pairs,
            f"{prefix}.AutoAcceptSharedAssociations",
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayMulticastDomainOptions:
    out: TransitGatewayMulticastDomainOptions = {}  # type: ignore[typeddict-item]
    child_igmpv2_support = el.find("Igmpv2Support")
    if child_igmpv2_support is not None:
        import aws_sdk_ec2.types.igmpv2_support_value

        out["igmpv2_support"] = (
            aws_sdk_ec2.types.igmpv2_support_value.deserialize_ec2_query(
                child_igmpv2_support
            )
        )
    child_static_sources_support = el.find("StaticSourcesSupport")
    if child_static_sources_support is not None:
        import aws_sdk_ec2.types.static_sources_support_value

        out["static_sources_support"] = (
            aws_sdk_ec2.types.static_sources_support_value.deserialize_ec2_query(
                child_static_sources_support
            )
        )
    child_auto_accept_shared_associations = el.find("AutoAcceptSharedAssociations")
    if child_auto_accept_shared_associations is not None:
        import aws_sdk_ec2.types.auto_accept_shared_associations_value

        out["auto_accept_shared_associations"] = (
            aws_sdk_ec2.types.auto_accept_shared_associations_value.deserialize_ec2_query(
                child_auto_accept_shared_associations
            )
        )
    return out
