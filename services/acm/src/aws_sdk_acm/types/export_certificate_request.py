"""Generated from Smithy shape ``com.amazonaws.acm#ExportCertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_acm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm.types.arn
    import aws_sdk_acm.types.passphrase_blob


class ExportCertificateRequest(TypedDict):
    certificate_arn: "aws_sdk_acm.types.arn.Arn"
    """<p>An Amazon Resource Name (ARN) of the issued certificate. This must be of the form:</p> <p> <code>arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012</code> </p>"""
    passphrase: "aws_sdk_acm.types.passphrase_blob.PassphraseBlob"
    """<p>Passphrase to associate with the encrypted exported private key. </p> <note> <p>When creating your passphrase, you can use any ASCII character except #, $, or %.</p> </note> <p>If you want to later decrypt the private key, you must have the passphrase. You can use the following OpenSSL command to decrypt a private key. After entering the command, you are prompted for the passphrase.</p> <p> <code>openssl rsa -in encrypted_key.pem -out decrypted_key.pem</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportCertificateRequest) -> dict:
    out: dict = {}
    out["CertificateArn"] = value["certificate_arn"]
    import aws_sdk_acm.types.passphrase_blob

    out["Passphrase"] = aws_sdk_acm.types.passphrase_blob.serialize_aws_json_1_1(
        value["passphrase"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportCertificateRequest:
    out: ExportCertificateRequest = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    else:
        raise DeserializationError("ExportCertificateRequest.certificate_arn required")
    if "Passphrase" in data:
        import aws_sdk_acm.types.passphrase_blob

        out["passphrase"] = aws_sdk_acm.types.passphrase_blob.deserialize_aws_json_1_1(
            data["Passphrase"]
        )
    else:
        raise DeserializationError("ExportCertificateRequest.passphrase required")
    return out
