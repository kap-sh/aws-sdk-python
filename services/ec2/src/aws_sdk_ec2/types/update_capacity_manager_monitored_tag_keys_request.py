"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateCapacityManagerMonitoredTagKeysRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class UpdateCapacityManagerMonitoredTagKeysRequest(TypedDict):
    activate_tag_keys: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p> The tag keys to activate for monitoring. Once activated, these tag keys will be included as dimensions in capacity metric data. </p>"""
    deactivate_tag_keys: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p> The tag keys to deactivate. Deactivated tag keys will no longer be included as dimensions in capacity metric data. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>"""
