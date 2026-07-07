"""Generated from Smithy shape ``com.amazonaws.forecast#S3Config``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.kms_key_arn
    import aws_sdk_forecast.types.s3_path


class S3Config(TypedDict, closed=True):
    path: "aws_sdk_forecast.types.s3_path.S3Path"
    """<p>The path to an Amazon Simple Storage Service (Amazon S3) bucket or file(s) in an Amazon S3 bucket.</p>"""
    role_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The ARN of the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the Amazon S3 bucket or files. If you provide a value for the <code>KMSKeyArn</code> key, the role must allow access to the key.</p> <p>Passing a role across Amazon Web Services accounts is not allowed. If you pass a role that isn't in your account, you get an <code>InvalidInputException</code> error.</p>"""
    kms_key_arn: NotRequired["aws_sdk_forecast.types.kms_key_arn.KMSKeyArn"]
    """<p>The Amazon Resource Name (ARN) of an Key Management Service (KMS) key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Config) -> dict:
    out: dict = {}
    out["Path"] = value["path"]
    out["RoleArn"] = value["role_arn"]
    if "kms_key_arn" in value:
        out["KMSKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Config:
    out: S3Config = {}  # type: ignore[typeddict-item]
    if "Path" in data:
        out["path"] = data["Path"]
    else:
        raise DeserializationError("S3Config.path required")
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("S3Config.role_arn required")
    if "KMSKeyArn" in data:
        out["kms_key_arn"] = data["KMSKeyArn"]
    return out
