"""Generated from Smithy shape ``com.amazonaws.forecast#EncryptionConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.kms_key_arn


class EncryptionConfig(TypedDict):
    role_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The ARN of the IAM role that Amazon Forecast can assume to access the KMS key.</p> <p>Passing a role across Amazon Web Services accounts is not allowed. If you pass a role that isn't in your account, you get an <code>InvalidInputException</code> error.</p>"""
    kms_key_arn: "aws_sdk_forecast.types.kms_key_arn.KMSKeyArn"
    """<p>The Amazon Resource Name (ARN) of the KMS key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionConfig) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    out["KMSKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionConfig:
    out: EncryptionConfig = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("EncryptionConfig.role_arn required")
    if "KMSKeyArn" in data:
        out["kms_key_arn"] = data["KMSKeyArn"]
    else:
        raise DeserializationError("EncryptionConfig.kms_key_arn required")
    return out
