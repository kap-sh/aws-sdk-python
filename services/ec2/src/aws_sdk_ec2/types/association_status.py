"""Generated from Smithy shape ``com.amazonaws.ec2#AssociationStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.association_status_code
    import aws_sdk_ec2.types.string


class AssociationStatus(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.association_status_code.AssociationStatusCode"]
    """<p>The state of the target network association.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message about the status of the target network association, if applicable.</p>"""
