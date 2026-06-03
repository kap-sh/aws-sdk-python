"""Generated from Smithy shape ``com.amazonaws.kms#AliasListEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.alias_name_type
    import awd_sdk_kms.types.arn_type
    import awd_sdk_kms.types.date_type
    import awd_sdk_kms.types.key_id_type


class AliasListEntry(TypedDict):
    alias_name: NotRequired["awd_sdk_kms.types.alias_name_type.AliasNameType"]
    """<p>String that contains the alias. This value begins with <code>alias/</code>.</p>"""
    alias_arn: NotRequired["awd_sdk_kms.types.arn_type.ArnType"]
    """<p>String that contains the key ARN.</p>"""
    target_key_id: NotRequired["awd_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>String that contains the key identifier of the KMS key associated with the alias.</p>"""
    creation_date: NotRequired["awd_sdk_kms.types.date_type.DateType"]
    """<p>Date and time that the alias was most recently created in the account and Region. Formatted as Unix time.</p>"""
    last_updated_date: NotRequired["awd_sdk_kms.types.date_type.DateType"]
    """<p>Date and time that the alias was most recently associated with a KMS key in the account and Region. Formatted as Unix time.</p>"""
