"""Generated from Smithy shape ``com.amazonaws.kms#Tag``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kms.types.tag_key_type
    import aws_sdk_kms.types.tag_value_type


class Tag(TypedDict):
    tag_key: "aws_sdk_kms.types.tag_key_type.TagKeyType"
    """<p>The key of the tag.</p>"""
    tag_value: "aws_sdk_kms.types.tag_value_type.TagValueType"
    """<p>The value of the tag.</p>"""
