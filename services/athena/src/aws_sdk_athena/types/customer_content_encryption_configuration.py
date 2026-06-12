"""Generated from Smithy shape ``com.amazonaws.athena#CustomerContentEncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.kms_key


class CustomerContentEncryptionConfiguration(TypedDict):
    kms_key: "aws_sdk_athena.types.kms_key.KmsKey"
    """<p>The customer managed KMS key that is used to encrypt the user's data stores in Athena.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerContentEncryptionConfiguration) -> dict:
    out: dict = {}
    out["KmsKey"] = value["kms_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerContentEncryptionConfiguration:
    out: CustomerContentEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "KmsKey" in data:
        out["kms_key"] = data["KmsKey"]
    else:
        raise DeserializationError(
            "CustomerContentEncryptionConfiguration.kms_key required"
        )
    return out
