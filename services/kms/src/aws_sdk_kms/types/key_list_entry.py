"""Generated from Smithy shape ``com.amazonaws.kms#KeyListEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.arn_type
    import aws_sdk_kms.types.key_id_type


class KeyListEntry(TypedDict):
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>Unique identifier of the key.</p>"""
    key_arn: NotRequired["aws_sdk_kms.types.arn_type.ArnType"]
    """<p>ARN of the key.</p>"""
