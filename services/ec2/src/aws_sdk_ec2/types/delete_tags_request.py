"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.resource_id_list
    import aws_sdk_ec2.types.tag_list


class DeleteTagsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    resources: NotRequired["aws_sdk_ec2.types.resource_id_list.ResourceIdList"]
    """<p>The IDs of the resources, separated by spaces.</p> <p>Constraints: Up to 1000 resource IDs. We recommend breaking up this request into smaller batches.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags to delete. Specify a tag key and an optional tag value to delete specific tags. If you specify a tag key without a tag value, we delete any tag with this key regardless of its value. If you specify a tag key with an empty string as the tag value, we delete the tag only if its value is an empty string.</p> <p>If you omit this parameter, we delete all user-defined tags for the specified resources. We do not delete Amazon Web Services-generated tags (tags that have the <code>aws:</code> prefix).</p> <p>Constraints: Up to 1000 tags.</p>"""
