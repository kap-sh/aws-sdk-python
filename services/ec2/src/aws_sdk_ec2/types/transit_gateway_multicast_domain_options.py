"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastDomainOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
