"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.verified_access_sse_specification_response


class VerifiedAccessGroup(TypedDict):
    verified_access_group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Verified Access group.</p>"""
    verified_access_instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services Verified Access instance.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the Amazon Web Services Verified Access group.</p>"""
    owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account number that owns the group.</p>"""
    verified_access_group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the Verified Access group.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The creation time.</p>"""
    last_updated_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The last updated time.</p>"""
    deletion_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The deletion time.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    sse_specification: NotRequired[
        "aws_sdk_ec2.types.verified_access_sse_specification_response.VerifiedAccessSseSpecificationResponse"
    ]
    """<p>The options in use for server side encryption.</p>"""
