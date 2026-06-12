"""Generated from Smithy shape ``com.amazonaws.athena#ManagedQueryResultsEncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.kms_key


class ManagedQueryResultsEncryptionConfiguration(TypedDict):
    kms_key: "aws_sdk_athena.types.kms_key.KmsKey"
    """<p>The ARN of an KMS key for encrypting managed query results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedQueryResultsEncryptionConfiguration) -> dict:
    out: dict = {}
    out["KmsKey"] = value["kms_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedQueryResultsEncryptionConfiguration:
    out: ManagedQueryResultsEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "KmsKey" in data:
        out["kms_key"] = data["KmsKey"]
    else:
        raise DeserializationError(
            "ManagedQueryResultsEncryptionConfiguration.kms_key required"
        )
    return out
