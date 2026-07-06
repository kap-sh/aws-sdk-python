"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateAuthority``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.account_id
    import aws_sdk_acm_pca.types.arn
    import aws_sdk_acm_pca.types.certificate_authority_configuration
    import aws_sdk_acm_pca.types.certificate_authority_status
    import aws_sdk_acm_pca.types.certificate_authority_type
    import aws_sdk_acm_pca.types.certificate_authority_usage_mode
    import aws_sdk_acm_pca.types.failure_reason
    import aws_sdk_acm_pca.types.key_storage_security_standard
    import aws_sdk_acm_pca.types.revocation_configuration
    import aws_sdk_acm_pca.types.string
    import aws_sdk_acm_pca.types.t_stamp


class CertificateAuthority(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_acm_pca.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) for your private certificate authority (CA). The format is <code> <i>12345678-1234-1234-1234-123456789012</i> </code>.</p>"""
    owner_account: NotRequired["aws_sdk_acm_pca.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that owns the certificate authority.</p>"""
    created_at: NotRequired["aws_sdk_acm_pca.types.t_stamp.TStamp"]
    """<p>Date and time at which your private CA was created.</p>"""
    last_state_change_at: NotRequired["aws_sdk_acm_pca.types.t_stamp.TStamp"]
    """<p>Date and time at which your private CA was last updated.</p>"""
    type: NotRequired[
        "aws_sdk_acm_pca.types.certificate_authority_type.CertificateAuthorityType"
    ]
    """<p>Type of your private CA.</p>"""
    serial: NotRequired["aws_sdk_acm_pca.types.string.String"]
    """<p>Serial number of your private CA.</p>"""
    status: NotRequired[
        "aws_sdk_acm_pca.types.certificate_authority_status.CertificateAuthorityStatus"
    ]
    """<p>Status of your private CA.</p>"""
    not_before: NotRequired["aws_sdk_acm_pca.types.t_stamp.TStamp"]
    """<p>Date and time before which your private CA certificate is not valid.</p>"""
    not_after: NotRequired["aws_sdk_acm_pca.types.t_stamp.TStamp"]
    """<p>Date and time after which your private CA certificate is not valid.</p>"""
    failure_reason: NotRequired["aws_sdk_acm_pca.types.failure_reason.FailureReason"]
    """<p>Reason the request to create your private CA failed.</p>"""
    certificate_authority_configuration: NotRequired[
        "aws_sdk_acm_pca.types.certificate_authority_configuration.CertificateAuthorityConfiguration"
    ]
    """<p>Your private CA configuration.</p>"""
    revocation_configuration: NotRequired[
        "aws_sdk_acm_pca.types.revocation_configuration.RevocationConfiguration"
    ]
    """<p>Information about the Online Certificate Status Protocol (OCSP) configuration or certificate revocation list (CRL) created and maintained by your private CA. </p>"""
    restorable_until: NotRequired["aws_sdk_acm_pca.types.t_stamp.TStamp"]
    r"""<p>The period during which a deleted CA can be restored. For more information, see the <code>PermanentDeletionTimeInDays</code> parameter of the <a href=\"https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthorityRequest.html\">DeleteCertificateAuthorityRequest</a> action. </p>"""
    key_storage_security_standard: NotRequired[
        "aws_sdk_acm_pca.types.key_storage_security_standard.KeyStorageSecurityStandard"
    ]
    r"""<p>Defines a cryptographic key management compliance standard for handling and protecting CA keys.</p> <p>Default: FIPS_140_2_LEVEL_3_OR_HIGHER</p> <note> <p>Starting January 26, 2023, Amazon Web Services Private CA protects all CA private keys in non-China regions using hardware security modules (HSMs) that comply with FIPS PUB 140-2 Level 3.</p> <p>For information about security standard support in different Amazon Web Services Regions, see <a href=\"https://docs.aws.amazon.com/privateca/latest/userguide/data-protection.html#private-keys\">Storage and security compliance of Amazon Web Services Private CA private keys</a>.</p> </note>"""
    usage_mode: NotRequired[
        "aws_sdk_acm_pca.types.certificate_authority_usage_mode.CertificateAuthorityUsageMode"
    ]
    """<p>Specifies whether the CA issues general-purpose certificates that typically require a revocation mechanism, or short-lived certificates that may optionally omit revocation because they expire quickly. Short-lived certificate validity is limited to seven days.</p> <p>The default value is GENERAL_PURPOSE.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateAuthority) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "owner_account" in value:
        out["OwnerAccount"] = value["owner_account"]
    if "created_at" in value:
        import aws_sdk_acm_pca.types.t_stamp

        out["CreatedAt"] = aws_sdk_acm_pca.types.t_stamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "last_state_change_at" in value:
        import aws_sdk_acm_pca.types.t_stamp

        out["LastStateChangeAt"] = aws_sdk_acm_pca.types.t_stamp.serialize_aws_json_1_1(
            value["last_state_change_at"]
        )
    if "type" in value:
        import aws_sdk_acm_pca.types.certificate_authority_type

        out["Type"] = (
            aws_sdk_acm_pca.types.certificate_authority_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "serial" in value:
        out["Serial"] = value["serial"]
    if "status" in value:
        import aws_sdk_acm_pca.types.certificate_authority_status

        out["Status"] = (
            aws_sdk_acm_pca.types.certificate_authority_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "not_before" in value:
        import aws_sdk_acm_pca.types.t_stamp

        out["NotBefore"] = aws_sdk_acm_pca.types.t_stamp.serialize_aws_json_1_1(
            value["not_before"]
        )
    if "not_after" in value:
        import aws_sdk_acm_pca.types.t_stamp

        out["NotAfter"] = aws_sdk_acm_pca.types.t_stamp.serialize_aws_json_1_1(
            value["not_after"]
        )
    if "failure_reason" in value:
        import aws_sdk_acm_pca.types.failure_reason

        out["FailureReason"] = (
            aws_sdk_acm_pca.types.failure_reason.serialize_aws_json_1_1(
                value["failure_reason"]
            )
        )
    if "certificate_authority_configuration" in value:
        import aws_sdk_acm_pca.types.certificate_authority_configuration

        out["CertificateAuthorityConfiguration"] = (
            aws_sdk_acm_pca.types.certificate_authority_configuration.serialize_aws_json_1_1(
                value["certificate_authority_configuration"]
            )
        )
    if "revocation_configuration" in value:
        import aws_sdk_acm_pca.types.revocation_configuration

        out["RevocationConfiguration"] = (
            aws_sdk_acm_pca.types.revocation_configuration.serialize_aws_json_1_1(
                value["revocation_configuration"]
            )
        )
    if "restorable_until" in value:
        import aws_sdk_acm_pca.types.t_stamp

        out["RestorableUntil"] = aws_sdk_acm_pca.types.t_stamp.serialize_aws_json_1_1(
            value["restorable_until"]
        )
    if "key_storage_security_standard" in value:
        import aws_sdk_acm_pca.types.key_storage_security_standard

        out["KeyStorageSecurityStandard"] = (
            aws_sdk_acm_pca.types.key_storage_security_standard.serialize_aws_json_1_1(
                value["key_storage_security_standard"]
            )
        )
    if "usage_mode" in value:
        import aws_sdk_acm_pca.types.certificate_authority_usage_mode

        out["UsageMode"] = (
            aws_sdk_acm_pca.types.certificate_authority_usage_mode.serialize_aws_json_1_1(
                value["usage_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateAuthority:
    out: CertificateAuthority = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "OwnerAccount" in data:
        out["owner_account"] = data["OwnerAccount"]
    if "CreatedAt" in data:
        import aws_sdk_acm_pca.types.t_stamp

        out["created_at"] = aws_sdk_acm_pca.types.t_stamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "LastStateChangeAt" in data:
        import aws_sdk_acm_pca.types.t_stamp

        out["last_state_change_at"] = (
            aws_sdk_acm_pca.types.t_stamp.deserialize_aws_json_1_1(
                data["LastStateChangeAt"]
            )
        )
    if "Type" in data:
        import aws_sdk_acm_pca.types.certificate_authority_type

        out["type"] = (
            aws_sdk_acm_pca.types.certificate_authority_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Serial" in data:
        out["serial"] = data["Serial"]
    if "Status" in data:
        import aws_sdk_acm_pca.types.certificate_authority_status

        out["status"] = (
            aws_sdk_acm_pca.types.certificate_authority_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "NotBefore" in data:
        import aws_sdk_acm_pca.types.t_stamp

        out["not_before"] = aws_sdk_acm_pca.types.t_stamp.deserialize_aws_json_1_1(
            data["NotBefore"]
        )
    if "NotAfter" in data:
        import aws_sdk_acm_pca.types.t_stamp

        out["not_after"] = aws_sdk_acm_pca.types.t_stamp.deserialize_aws_json_1_1(
            data["NotAfter"]
        )
    if "FailureReason" in data:
        import aws_sdk_acm_pca.types.failure_reason

        out["failure_reason"] = (
            aws_sdk_acm_pca.types.failure_reason.deserialize_aws_json_1_1(
                data["FailureReason"]
            )
        )
    if "CertificateAuthorityConfiguration" in data:
        import aws_sdk_acm_pca.types.certificate_authority_configuration

        out["certificate_authority_configuration"] = (
            aws_sdk_acm_pca.types.certificate_authority_configuration.deserialize_aws_json_1_1(
                data["CertificateAuthorityConfiguration"]
            )
        )
    if "RevocationConfiguration" in data:
        import aws_sdk_acm_pca.types.revocation_configuration

        out["revocation_configuration"] = (
            aws_sdk_acm_pca.types.revocation_configuration.deserialize_aws_json_1_1(
                data["RevocationConfiguration"]
            )
        )
    if "RestorableUntil" in data:
        import aws_sdk_acm_pca.types.t_stamp

        out["restorable_until"] = (
            aws_sdk_acm_pca.types.t_stamp.deserialize_aws_json_1_1(
                data["RestorableUntil"]
            )
        )
    if "KeyStorageSecurityStandard" in data:
        import aws_sdk_acm_pca.types.key_storage_security_standard

        out["key_storage_security_standard"] = (
            aws_sdk_acm_pca.types.key_storage_security_standard.deserialize_aws_json_1_1(
                data["KeyStorageSecurityStandard"]
            )
        )
    if "UsageMode" in data:
        import aws_sdk_acm_pca.types.certificate_authority_usage_mode

        out["usage_mode"] = (
            aws_sdk_acm_pca.types.certificate_authority_usage_mode.deserialize_aws_json_1_1(
                data["UsageMode"]
            )
        )
    return out
