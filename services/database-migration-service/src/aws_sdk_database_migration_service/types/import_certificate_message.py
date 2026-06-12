"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ImportCertificateMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.certificate_wallet
    import aws_sdk_database_migration_service.types.secret_string
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.tag_list


class ImportCertificateMessage(TypedDict):
    certificate_identifier: "aws_sdk_database_migration_service.types.string.String"
    """<p>A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.</p>"""
    certificate_pem: NotRequired[
        "aws_sdk_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>The contents of a <code>.pem</code> file, which contains an X.509 certificate.</p>"""
    certificate_wallet: NotRequired[
        "aws_sdk_database_migration_service.types.certificate_wallet.CertificateWallet"
    ]
    """<p>The location of an imported Oracle Wallet certificate for use with SSL. Provide the name of a <code>.sso</code> file using the <code>fileb://</code> prefix. You can't provide the certificate inline.</p> <p>Example: <code>filebase64(\"${path.root}/rds-ca-2019-root.sso\")</code> </p>"""
    tags: NotRequired["aws_sdk_database_migration_service.types.tag_list.TagList"]
    """<p>The tags associated with the certificate.</p>"""
    kms_key_id: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>An KMS key identifier that is used to encrypt the certificate.</p> <p>If you don't specify a value for the <code>KmsKeyId</code> parameter, then DMS uses your default encryption key.</p> <p>KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportCertificateMessage) -> dict:
    out: dict = {}
    out["CertificateIdentifier"] = value["certificate_identifier"]
    if "certificate_pem" in value:
        out["CertificatePem"] = value["certificate_pem"]
    if "certificate_wallet" in value:
        import aws_sdk_database_migration_service.types.certificate_wallet

        out["CertificateWallet"] = (
            aws_sdk_database_migration_service.types.certificate_wallet.serialize_aws_json_1_1(
                value["certificate_wallet"]
            )
        )
    if "tags" in value:
        import aws_sdk_database_migration_service.types.tag_list

        out["Tags"] = (
            aws_sdk_database_migration_service.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportCertificateMessage:
    out: ImportCertificateMessage = {}  # type: ignore[typeddict-item]
    if "CertificateIdentifier" in data:
        out["certificate_identifier"] = data["CertificateIdentifier"]
    else:
        raise DeserializationError(
            "ImportCertificateMessage.certificate_identifier required"
        )
    if "CertificatePem" in data:
        out["certificate_pem"] = data["CertificatePem"]
    if "CertificateWallet" in data:
        import aws_sdk_database_migration_service.types.certificate_wallet

        out["certificate_wallet"] = (
            aws_sdk_database_migration_service.types.certificate_wallet.deserialize_aws_json_1_1(
                data["CertificateWallet"]
            )
        )
    if "Tags" in data:
        import aws_sdk_database_migration_service.types.tag_list

        out["tags"] = (
            aws_sdk_database_migration_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
