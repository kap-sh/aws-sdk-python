"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessInstanceResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_instance


class CreateVerifiedAccessInstanceResult(TypedDict):
    verified_access_instance: NotRequired[
        "aws_sdk_ec2.types.verified_access_instance.VerifiedAccessInstance"
    ]
    """<p>Details about the Verified Access instance.</p>"""
