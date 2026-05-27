"""Generated from Smithy shape ``com.amazonaws.ec2#GetAllowedImagesSettingsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_criterion_list
    import aws_sdk_ec2.types.managed_by
    import aws_sdk_ec2.types.string


class GetAllowedImagesSettingsResult(TypedDict):
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The current state of the Allowed AMIs setting at the account level in the specified Amazon Web Services Region.</p> <p>Possible values:</p> <ul> <li> <p> <code>disabled</code>: All AMIs are allowed.</p> </li> <li> <p> <code>audit-mode</code>: All AMIs are allowed, but the <code>ImageAllowed</code> field is set to <code>true</code> if the AMI would be allowed with the current list of criteria if allowed AMIs was enabled.</p> </li> <li> <p> <code>enabled</code>: Only AMIs matching the image criteria are discoverable and available for use.</p> </li> </ul>"""
    image_criteria: NotRequired[
        "aws_sdk_ec2.types.image_criterion_list.ImageCriterionList"
    ]
    """<p>The list of criteria for images that are discoverable and usable in the account in the specified Amazon Web Services Region.</p>"""
    managed_by: NotRequired["aws_sdk_ec2.types.managed_by.ManagedBy"]
    """<p>The entity that manages the Allowed AMIs settings. Possible values include:</p> <ul> <li> <p> <code>account</code> - The Allowed AMIs settings is managed by the account.</p> </li> <li> <p> <code>declarative-policy</code> - The Allowed AMIs settings is managed by a declarative policy and can't be modified by the account.</p> </li> </ul>"""
