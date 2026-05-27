"""Generated from Smithy shape ``com.amazonaws.ec2#UserData``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class UserData(TypedDict):
    data: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The user data. If you are using an Amazon Web Services SDK or command line tool, Base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide Base64-encoded text.</p>"""
