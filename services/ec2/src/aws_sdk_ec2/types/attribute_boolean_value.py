"""Generated from Smithy shape ``com.amazonaws.ec2#AttributeBooleanValue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class AttributeBooleanValue(TypedDict):
    value: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The attribute value. The valid values are <code>true</code> or <code>false</code>.</p>"""
