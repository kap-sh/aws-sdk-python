"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstance``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.verified_access_instance_custom_sub_domain
    import aws_sdk_ec2.types.verified_access_trust_provider_condensed_list


class VerifiedAccessInstance(TypedDict):
    verified_access_instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services Verified Access instance.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the Amazon Web Services Verified Access instance.</p>"""
    verified_access_trust_providers: NotRequired[
        "aws_sdk_ec2.types.verified_access_trust_provider_condensed_list.VerifiedAccessTrustProviderCondensedList"
    ]
    """<p>The IDs of the Amazon Web Services Verified Access trust providers.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The creation time.</p>"""
    last_updated_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The last updated time.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    fips_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether support for Federal Information Processing Standards (FIPS) is enabled on the instance.</p>"""
    cidr_endpoints_custom_sub_domain: NotRequired[
        "aws_sdk_ec2.types.verified_access_instance_custom_sub_domain.VerifiedAccessInstanceCustomSubDomain"
    ]
    """<p>The custom subdomain.</p>"""
