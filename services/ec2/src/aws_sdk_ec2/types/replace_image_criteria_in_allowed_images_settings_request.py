"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceImageCriteriaInAllowedImagesSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_criterion_request_list


class ReplaceImageCriteriaInAllowedImagesSettingsRequest(TypedDict):
    image_criteria: NotRequired[
        "aws_sdk_ec2.types.image_criterion_request_list.ImageCriterionRequestList"
    ]
    """<p>The list of criteria that are evaluated to determine whether AMIs are discoverable and usable in the account in the specified Amazon Web Services Region.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
