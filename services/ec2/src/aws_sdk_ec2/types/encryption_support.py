"""Generated from Smithy shape ``com.amazonaws.ec2#EncryptionSupport``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.encryption_state_value
    import aws_sdk_ec2.types.string


class EncryptionSupport(TypedDict):
    encryption_state: NotRequired[
        "aws_sdk_ec2.types.encryption_state_value.EncryptionStateValue"
    ]
    """<p>The current encryption state of the resource.</p>"""
    state_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message describing the encryption state.</p>"""
