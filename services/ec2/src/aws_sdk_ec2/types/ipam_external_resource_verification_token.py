"""Generated from Smithy shape ``com.amazonaws.ec2#IpamExternalResourceVerificationToken``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_external_resource_verification_token_id
    import aws_sdk_ec2.types.ipam_external_resource_verification_token_state
    import aws_sdk_ec2.types.ipam_id
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.token_state


class IpamExternalResourceVerificationToken(TypedDict):
    ipam_external_resource_verification_token_id: NotRequired[
        "aws_sdk_ec2.types.ipam_external_resource_verification_token_id.IpamExternalResourceVerificationTokenId"
    ]
    """<p>The ID of the token.</p>"""
    ipam_external_resource_verification_token_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>Token ARN.</p>"""
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM that created the token.</p>"""
    ipam_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>ARN of the IPAM that created the token.</p>"""
    ipam_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Region of the IPAM that created the token.</p>"""
    token_value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Token value.</p>"""
    token_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Token name.</p>"""
    not_after: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Token expiration.</p>"""
    status: NotRequired["aws_sdk_ec2.types.token_state.TokenState"]
    """<p>Token status.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Token tags.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.ipam_external_resource_verification_token_state.IpamExternalResourceVerificationTokenState"
    ]
    """<p>Token state.</p>"""
