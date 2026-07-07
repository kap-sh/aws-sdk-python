"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsKinesisStreamStreamEncryptionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsKinesisStreamStreamEncryptionDetails(TypedDict, closed=True):
    encryption_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The encryption type to use. </p>"""
    key_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The globally unique identifier for the customer-managed KMS key to use for encryption. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsKinesisStreamStreamEncryptionDetails) -> dict:
    out: dict = {}
    if "encryption_type" in value:
        out["EncryptionType"] = value["encryption_type"]
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    return out


def deserialize_json(data: dict) -> AwsKinesisStreamStreamEncryptionDetails:
    out: AwsKinesisStreamStreamEncryptionDetails = {}  # type: ignore[typeddict-item]
    if "EncryptionType" in data:
        out["encryption_type"] = data["EncryptionType"]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    return out
