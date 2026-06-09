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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecretVersionsListEntry) -> dict:
    out: dict = {}
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "version_stages" in value:
        import aws_sdk_secrets_manager.types.secret_version_stages_type

        out["VersionStages"] = (
            aws_sdk_secrets_manager.types.secret_version_stages_type.serialize_aws_json_1_1(
                value["version_stages"]
            )
        )
    if "last_accessed_date" in value:
        import aws_sdk_secrets_manager.types.last_accessed_date_type

        out["LastAccessedDate"] = (
            aws_sdk_secrets_manager.types.last_accessed_date_type.serialize_aws_json_1_1(
                value["last_accessed_date"]
            )
        )
    if "created_date" in value:
        import aws_sdk_secrets_manager.types.created_date_type

        out["CreatedDate"] = (
            aws_sdk_secrets_manager.types.created_date_type.serialize_aws_json_1_1(
                value["created_date"]
            )
        )
    if "kms_key_ids" in value:
        import aws_sdk_secrets_manager.types.kms_key_id_list_type

        out["KmsKeyIds"] = (
            aws_sdk_secrets_manager.types.kms_key_id_list_type.serialize_aws_json_1_1(
                value["kms_key_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SecretVersionsListEntry:
    out: SecretVersionsListEntry = {}  # type: ignore[typeddict-item]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    if "VersionStages" in data:
        import aws_sdk_secrets_manager.types.secret_version_stages_type

        out["version_stages"] = (
            aws_sdk_secrets_manager.types.secret_version_stages_type.deserialize_aws_json_1_1(
                data["VersionStages"]
            )
        )
    if "LastAccessedDate" in data:
        import aws_sdk_secrets_manager.types.last_accessed_date_type

        out["last_accessed_date"] = (
            aws_sdk_secrets_manager.types.last_accessed_date_type.deserialize_aws_json_1_1(
                data["LastAccessedDate"]
            )
        )
    if "CreatedDate" in data:
        import aws_sdk_secrets_manager.types.created_date_type

        out["created_date"] = (
            aws_sdk_secrets_manager.types.created_date_type.deserialize_aws_json_1_1(
                data["CreatedDate"]
            )
        )
    if "KmsKeyIds" in data:
        import aws_sdk_secrets_manager.types.kms_key_id_list_type

        out["kms_key_ids"] = (
            aws_sdk_secrets_manager.types.kms_key_id_list_type.deserialize_aws_json_1_1(
                data["KmsKeyIds"]
            )
        )
    return out
