"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttributeValue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AccountAttributeValue(TypedDict):
    attribute_value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The value of the attribute.</p>"""
