"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetParametersForImportOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.certificate_type
    import aws_sdk_payment_cryptography.types.import_token_id
    import aws_sdk_payment_cryptography.types.key_algorithm
    import aws_sdk_payment_cryptography.types.timestamp


class GetParametersForImportOutput(TypedDict):
    wrapping_key_certificate: (
        "aws_sdk_payment_cryptography.types.certificate_type.CertificateType"
    )
    """<p>The wrapping key certificate in PEM format (base64 encoded) of the wrapping key for use within the TR-34 key block. The certificate expires in 30 days.</p>"""
    wrapping_key_certificate_chain: (
        "aws_sdk_payment_cryptography.types.certificate_type.CertificateType"
    )
    """<p>The Amazon Web Services Payment Cryptography root certificate authority (CA) that signed the wrapping key certificate in PEM format (base64 encoded).</p>"""
    wrapping_key_algorithm: (
        "aws_sdk_payment_cryptography.types.key_algorithm.KeyAlgorithm"
    )
    """<p>The algorithm of the wrapping key for use within TR-34 WrappedKeyBlock or RSA WrappedKeyCryptogram.</p>"""
    import_token: "aws_sdk_payment_cryptography.types.import_token_id.ImportTokenId"
    """<p>The import token to initiate key import into Amazon Web Services Payment Cryptography. The import token expires after 30 days. You can use the same import token to import multiple keys to the same service account.</p>"""
    parameters_valid_until_timestamp: (
        "aws_sdk_payment_cryptography.types.timestamp.Timestamp"
    )
    """<p>The validity period of the import token.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetParametersForImportOutput) -> dict:
    out: dict = {}
    out["WrappingKeyCertificate"] = value["wrapping_key_certificate"]
    out["WrappingKeyCertificateChain"] = value["wrapping_key_certificate_chain"]
    out["WrappingKeyAlgorithm"] = value["wrapping_key_algorithm"]
    out["ImportToken"] = value["import_token"]
    import aws_sdk_payment_cryptography.types.timestamp

    out["ParametersValidUntilTimestamp"] = (
        aws_sdk_payment_cryptography.types.timestamp.serialize_aws_json_1_0(
            value["parameters_valid_until_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetParametersForImportOutput:
    out: GetParametersForImportOutput = {}  # type: ignore[typeddict-item]
    if "WrappingKeyCertificate" in data:
        out["wrapping_key_certificate"] = data["WrappingKeyCertificate"]
    else:
        raise DeserializationError(
            "GetParametersForImportOutput.wrapping_key_certificate required"
        )
    if "WrappingKeyCertificateChain" in data:
        out["wrapping_key_certificate_chain"] = data["WrappingKeyCertificateChain"]
    else:
        raise DeserializationError(
            "GetParametersForImportOutput.wrapping_key_certificate_chain required"
        )
    if "WrappingKeyAlgorithm" in data:
        out["wrapping_key_algorithm"] = data["WrappingKeyAlgorithm"]
    else:
        raise DeserializationError(
            "GetParametersForImportOutput.wrapping_key_algorithm required"
        )
    if "ImportToken" in data:
        out["import_token"] = data["ImportToken"]
    else:
        raise DeserializationError("GetParametersForImportOutput.import_token required")
    if "ParametersValidUntilTimestamp" in data:
        import aws_sdk_payment_cryptography.types.timestamp

        out["parameters_valid_until_timestamp"] = (
            aws_sdk_payment_cryptography.types.timestamp.deserialize_aws_json_1_0(
                data["ParametersValidUntilTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "GetParametersForImportOutput.parameters_valid_until_timestamp required"
        )
    return out
