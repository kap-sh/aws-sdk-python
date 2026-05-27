"""Generated from Smithy shape ``com.amazonaws.ec2#CreateManagedPrefixListRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.add_prefix_list_entries
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateManagedPrefixListRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    prefix_list_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A name for the prefix list.</p> <p>Constraints: Up to 255 characters in length. The name cannot start with <code>com.amazonaws</code>.</p>"""
    entries: NotRequired[
        "aws_sdk_ec2.types.add_prefix_list_entries.AddPrefixListEntries"
    ]
    """<p>One or more entries for the prefix list.</p>"""
    max_entries: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of entries for the prefix list.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the prefix list during creation.</p>"""
    address_family: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP address type.</p> <p>Valid Values: <code>IPv4</code> | <code>IPv6</code> </p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p> <p>Constraints: Up to 255 UTF-8 characters in length.</p>"""
