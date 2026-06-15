"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#Certificate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.certificate_wallet
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.t_stamp


class Certificate(TypedDict):
    certificate_identifier: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.</p>"""
    certificate_creation_date: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date that the certificate was created.</p>"""
    certificate_pem: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The contents of a <code>.pem</code> file, which contains an X.509 certificate.</p>"""
    certificate_wallet: NotRequired[
        "aws_sdk_database_migration_service.types.certificate_wallet.CertificateWallet"
    ]
    r"""<p>The location of an imported Oracle Wallet certificate for use with SSL. Example: <code>filebase64(\"${path.root}/rds-ca-2019-root.sso\")</code> </p>"""
    certificate_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) for the certificate.</p>"""
    certificate_owner: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The owner of the certificate.</p>"""
    valid_from_date: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The beginning date that the certificate is valid.</p>"""
    valid_to_date: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The final date that the certificate is valid.</p>"""
    signing_algorithm: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The signing algorithm for the certificate.</p>"""
    key_length: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The key length of the cryptographic algorithm being used.</p>"""
    kms_key_id: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>An KMS key identifier that is used to encrypt the certificate.</p> <p>If you don't specify a value for the <code>KmsKeyId</code> parameter, then DMS uses your default encryption key.</p> <p>KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Certificate) -> dict:
    out: dict = {}
    if "certificate_identifier" in value:
        out["CertificateIdentifier"] = value["certificate_identifier"]
    if "certificate_creation_date" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["CertificateCreationDate"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["certificate_creation_date"]
            )
        )
    if "certificate_pem" in value:
        out["CertificatePem"] = value["certificate_pem"]
    if "certificate_wallet" in value:
        import aws_sdk_database_migration_service.types.certificate_wallet

        out["CertificateWallet"] = (
            aws_sdk_database_migration_service.types.certificate_wallet.serialize_aws_json_1_1(
                value["certificate_wallet"]
            )
        )
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "certificate_owner" in value:
        out["CertificateOwner"] = value["certificate_owner"]
    if "valid_from_date" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["ValidFromDate"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["valid_from_date"]
            )
        )
    if "valid_to_date" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["ValidToDate"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["valid_to_date"]
            )
        )
    if "signing_algorithm" in value:
        out["SigningAlgorithm"] = value["signing_algorithm"]
    if "key_length" in value:
        out["KeyLength"] = value["key_length"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    if "CertificateIdentifier" in data:
        out["certificate_identifier"] = data["CertificateIdentifier"]
    if "CertificateCreationDate" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["certificate_creation_date"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["CertificateCreationDate"]
            )
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
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    if "CertificateOwner" in data:
        out["certificate_owner"] = data["CertificateOwner"]
    if "ValidFromDate" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["valid_from_date"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ValidFromDate"]
            )
        )
    if "ValidToDate" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["valid_to_date"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ValidToDate"]
            )
        )
    if "SigningAlgorithm" in data:
        out["signing_algorithm"] = data["SigningAlgorithm"]
    if "KeyLength" in data:
        out["key_length"] = data["KeyLength"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
