"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#KerberosAuthenticationSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class KerberosAuthenticationSettings(TypedDict):
    key_cache_secret_id: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>Specifies the ID of the secret that stores the key cache file required for kerberos authentication.</p>"""
    key_cache_secret_iam_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>Specifies the Amazon Resource Name (ARN) of the IAM role that grants Amazon Web Services DMS access to the secret containing key cache file for the kerberos authentication.</p>"""
    krb5_file_contents: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>Specifies the contents of krb5 configuration file required for kerberos authentication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KerberosAuthenticationSettings) -> dict:
    out: dict = {}
    if "key_cache_secret_id" in value:
        out["KeyCacheSecretId"] = value["key_cache_secret_id"]
    if "key_cache_secret_iam_arn" in value:
        out["KeyCacheSecretIamArn"] = value["key_cache_secret_iam_arn"]
    if "krb5_file_contents" in value:
        out["Krb5FileContents"] = value["krb5_file_contents"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KerberosAuthenticationSettings:
    out: KerberosAuthenticationSettings = {}  # type: ignore[typeddict-item]
    if "KeyCacheSecretId" in data:
        out["key_cache_secret_id"] = data["KeyCacheSecretId"]
    if "KeyCacheSecretIamArn" in data:
        out["key_cache_secret_iam_arn"] = data["KeyCacheSecretIamArn"]
    if "Krb5FileContents" in data:
        out["krb5_file_contents"] = data["Krb5FileContents"]
    return out
