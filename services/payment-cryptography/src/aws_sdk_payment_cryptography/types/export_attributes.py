"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ExportAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.export_dukpt_initial_key
    import aws_sdk_payment_cryptography.types.key_check_value_algorithm


class ExportAttributes(TypedDict, closed=True):
    export_dukpt_initial_key: NotRequired[
        "aws_sdk_payment_cryptography.types.export_dukpt_initial_key.ExportDukptInitialKey"
    ]
    """<p>Parameter information for IPEK export.</p>"""
    key_check_value_algorithm: NotRequired[
        "aws_sdk_payment_cryptography.types.key_check_value_algorithm.KeyCheckValueAlgorithm"
    ]
    """<p>The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity. Specify KCV for IPEK export only.</p> <p>For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result. For HMAC keys, the KCV is computed using the hash selected at key creation on a zero-length message, taking the leftmost 3 bytes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportAttributes) -> dict:
    out: dict = {}
    if "export_dukpt_initial_key" in value:
        import aws_sdk_payment_cryptography.types.export_dukpt_initial_key

        out["ExportDukptInitialKey"] = (
            aws_sdk_payment_cryptography.types.export_dukpt_initial_key.serialize_aws_json_1_0(
                value["export_dukpt_initial_key"]
            )
        )
    if "key_check_value_algorithm" in value:
        out["KeyCheckValueAlgorithm"] = value["key_check_value_algorithm"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportAttributes:
    out: ExportAttributes = {}  # type: ignore[typeddict-item]
    if "ExportDukptInitialKey" in data:
        import aws_sdk_payment_cryptography.types.export_dukpt_initial_key

        out["export_dukpt_initial_key"] = (
            aws_sdk_payment_cryptography.types.export_dukpt_initial_key.deserialize_aws_json_1_0(
                data["ExportDukptInitialKey"]
            )
        )
    if "KeyCheckValueAlgorithm" in data:
        out["key_check_value_algorithm"] = data["KeyCheckValueAlgorithm"]
    return out
