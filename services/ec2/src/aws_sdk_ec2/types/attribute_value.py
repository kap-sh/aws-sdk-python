"""Generated from Smithy shape ``com.amazonaws.ec2#AttributeValue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AttributeValue(TypedDict):
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The attribute value. The value is case-sensitive.</p>"""
