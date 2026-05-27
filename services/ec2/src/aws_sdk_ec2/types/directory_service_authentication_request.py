"""Generated from Smithy shape ``com.amazonaws.ec2#DirectoryServiceAuthenticationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class DirectoryServiceAuthenticationRequest(TypedDict):
    directory_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Active Directory to be used for authentication.</p>"""
