"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetKMSEncryptionKeyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.kms_key


class GetKMSEncryptionKeyResult(TypedDict, closed=True):
    kms_key: NotRequired["aws_sdk_frauddetector.types.kms_key.KMSKey"]
    """<p>The KMS encryption key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetKMSEncryptionKeyResult) -> dict:
    out: dict = {}
    if "kms_key" in value:
        import aws_sdk_frauddetector.types.kms_key

        out["kmsKey"] = aws_sdk_frauddetector.types.kms_key.serialize_aws_json_1_1(
            value["kms_key"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetKMSEncryptionKeyResult:
    out: GetKMSEncryptionKeyResult = {}  # type: ignore[typeddict-item]
    if "kmsKey" in data:
        import aws_sdk_frauddetector.types.kms_key

        out["kms_key"] = aws_sdk_frauddetector.types.kms_key.deserialize_aws_json_1_1(
            data["kmsKey"]
        )
    return out
