"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessGroupResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_group


class ModifyVerifiedAccessGroupResult(TypedDict):
    verified_access_group: NotRequired[
        "aws_sdk_ec2.types.verified_access_group.VerifiedAccessGroup"
    ]
    """<p>Details about the Verified Access group.</p>"""
