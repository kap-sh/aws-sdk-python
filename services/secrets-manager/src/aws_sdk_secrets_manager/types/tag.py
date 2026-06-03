"""Generated from Smithy shape ``com.amazonaws.secretsmanager#Tag``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.tag_key_type
    import aws_sdk_secrets_manager.types.tag_value_type


class Tag(TypedDict):
    key: NotRequired["aws_sdk_secrets_manager.types.tag_key_type.TagKeyType"]
    """<p>The key identifier, or name, of the tag.</p>"""
    value: NotRequired["aws_sdk_secrets_manager.types.tag_value_type.TagValueType"]
    """<p>The string value associated with the key of the tag.</p>"""
