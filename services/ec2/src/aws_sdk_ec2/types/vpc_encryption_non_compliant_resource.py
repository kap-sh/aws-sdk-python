"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionNonCompliantResource``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class VpcEncryptionNonCompliantResource(TypedDict):
    id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the non-compliant resource.</p>"""
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of the non-compliant resource.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the non-compliant resource.</p>"""
    is_excludable: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the resource can be excluded from encryption enforcement.</p>"""
