"""Generated from Smithy shape ``com.amazonaws.ec2#Phase2EncryptionAlgorithmsListValue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class Phase2EncryptionAlgorithmsListValue(TypedDict):
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The encryption algorithm.</p>"""
