"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetParametersForExportOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.certificate_type
    import aws_sdk_payment_cryptography.types.export_token_id
    import aws_sdk_payment_cryptography.types.key_algorithm
    import aws_sdk_payment_cryptography.types.timestamp


class GetParametersForExportOutput(TypedDict, closed=True):
    signing_key_certificate: (
        "aws_sdk_payment_cryptography.types.certificate_type.CertificateType"
    )
    """<p>The signing key certificate in PEM format (base64 encoded) of the public key for signature within the TR-34 key block. The certificate expires after 30 days.</p>"""
    signing_key_certificate_chain: (
        "aws_sdk_payment_cryptography.types.certificate_type.CertificateType"
    )
    """<p>The root certificate authority (CA) that signed the signing key certificate in PEM format (base64 encoded).</p>"""
    signing_key_algorithm: (
        "aws_sdk_payment_cryptography.types.key_algorithm.KeyAlgorithm"
    )
    """<p>The algorithm of the signing key certificate for use in TR-34 key block generation. <code>RSA_2048</code> is the only signing key algorithm allowed.</p>"""
    export_token: "aws_sdk_payment_cryptography.types.export_token_id.ExportTokenId"
    """<p>The export token to initiate key export from Amazon Web Services Payment Cryptography. The export token expires after 30 days. You can use the same export token to export multiple keys from the same service account.</p>"""
    parameters_valid_until_timestamp: (
        "aws_sdk_payment_cryptography.types.timestamp.Timestamp"
    )
    """<p>The validity period of the export token.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetParametersForExportOutput) -> dict:
    out: dict = {}
    out["SigningKeyCertificate"] = value["signing_key_certificate"]
    out["SigningKeyCertificateChain"] = value["signing_key_certificate_chain"]
    out["SigningKeyAlgorithm"] = value["signing_key_algorithm"]
    out["ExportToken"] = value["export_token"]
    import aws_sdk_payment_cryptography.types.timestamp

    out["ParametersValidUntilTimestamp"] = (
        aws_sdk_payment_cryptography.types.timestamp.serialize_aws_json_1_0(
            value["parameters_valid_until_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetParametersForExportOutput:
    out: GetParametersForExportOutput = {}  # type: ignore[typeddict-item]
    if "SigningKeyCertificate" in data:
        out["signing_key_certificate"] = data["SigningKeyCertificate"]
    else:
        raise DeserializationError(
            "GetParametersForExportOutput.signing_key_certificate required"
        )
    if "SigningKeyCertificateChain" in data:
        out["signing_key_certificate_chain"] = data["SigningKeyCertificateChain"]
    else:
        raise DeserializationError(
            "GetParametersForExportOutput.signing_key_certificate_chain required"
        )
    if "SigningKeyAlgorithm" in data:
        out["signing_key_algorithm"] = data["SigningKeyAlgorithm"]
    else:
        raise DeserializationError(
            "GetParametersForExportOutput.signing_key_algorithm required"
        )
    if "ExportToken" in data:
        out["export_token"] = data["ExportToken"]
    else:
        raise DeserializationError("GetParametersForExportOutput.export_token required")
    if "ParametersValidUntilTimestamp" in data:
        import aws_sdk_payment_cryptography.types.timestamp

        out["parameters_valid_until_timestamp"] = (
            aws_sdk_payment_cryptography.types.timestamp.deserialize_aws_json_1_0(
                data["ParametersValidUntilTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "GetParametersForExportOutput.parameters_valid_until_timestamp required"
        )
    return out
