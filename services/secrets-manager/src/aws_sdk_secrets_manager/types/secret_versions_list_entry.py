"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretVersionsListEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.created_date_type
    import aws_sdk_secrets_manager.types.kms_key_id_list_type
    import aws_sdk_secrets_manager.types.last_accessed_date_type
    import aws_sdk_secrets_manager.types.secret_version_id_type
    import aws_sdk_secrets_manager.types.secret_version_stages_type


class SecretVersionsListEntry(TypedDict):
    version_id: NotRequired[
        "aws_sdk_secrets_manager.types.secret_version_id_type.SecretVersionIdType"
    ]
    """<p>The unique version identifier of this version of the secret.</p>"""
    version_stages: NotRequired[
        "aws_sdk_secrets_manager.types.secret_version_stages_type.SecretVersionStagesType"
    ]
    """<p>An array of staging labels that are currently associated with this version of the secret.</p>"""
    last_accessed_date: NotRequired[
        "aws_sdk_secrets_manager.types.last_accessed_date_type.LastAccessedDateType"
    ]
    """<p>The date that this version of the secret was last accessed. Note that the resolution of this field is at the date level and does not include the time.</p>"""
    created_date: NotRequired[
        "aws_sdk_secrets_manager.types.created_date_type.CreatedDateType"
    ]
    """<p>The date and time this version of the secret was created.</p>"""
    kms_key_ids: NotRequired[
        "aws_sdk_secrets_manager.types.kms_key_id_list_type.KmsKeyIdListType"
    ]
    """<p>The KMS keys used to encrypt the secret version.</p>"""
