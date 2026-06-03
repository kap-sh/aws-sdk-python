"""Generated from Smithy shape ``com.amazonaws.kms#Tag``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import awd_sdk_kms.types.tag_key_type
    import awd_sdk_kms.types.tag_value_type


class Tag(TypedDict):
    tag_key: "awd_sdk_kms.types.tag_key_type.TagKeyType"
    """<p>The key of the tag.</p>"""
    tag_value: "awd_sdk_kms.types.tag_value_type.TagValueType"
    """<p>The value of the tag.</p>"""
