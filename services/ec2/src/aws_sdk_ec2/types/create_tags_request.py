"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.resource_id_list
    import aws_sdk_ec2.types.tag_list


class CreateTagsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    resources: NotRequired["aws_sdk_ec2.types.resource_id_list.ResourceIdList"]
    """<p>The IDs of the resources, separated by spaces.</p> <p>Constraints: Up to 1000 resource IDs. We recommend breaking up this request into smaller batches.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags. The <code>value</code> parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.</p>"""
