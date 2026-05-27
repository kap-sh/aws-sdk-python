"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateAddressResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AssociateAddressResult(TypedDict):
    association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID that represents the association of the Elastic IP address with an instance.</p>"""
