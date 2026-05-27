"""Generated from Smithy shape ``com.amazonaws.ec2#DirectoryServiceAuthentication``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class DirectoryServiceAuthentication(TypedDict):
    directory_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Active Directory used for authentication.</p>"""
