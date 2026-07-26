"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#S3ConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.s3_arn_type


class S3ConfigurationType(TypedDict, closed=True):
    bucket_arn: NotRequired[
        "capo_cognito_identity_provider.types.s3_arn_type.S3ArnType"
    ]
    """<p>The ARN of an Amazon S3 bucket that's the destination for threat protection log export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ConfigurationType) -> dict:
    out: dict = {}
    if "bucket_arn" in value:
        out["BucketArn"] = value["bucket_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ConfigurationType:
    out: S3ConfigurationType = {}  # type: ignore[typeddict-item]
    if "BucketArn" in data:
        out["bucket_arn"] = data["BucketArn"]
    return out
