"""Generated from Smithy shape ``com.amazonaws.datasync#CustomSecretConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.iam_role_arn_or_empty_string
    import aws_sdk_datasync.types.secret_arn


class CustomSecretConfig(TypedDict):
    secret_arn: NotRequired["aws_sdk_datasync.types.secret_arn.SecretArn"]
    """<p>Specifies the ARN for an Secrets Manager secret.</p>"""
    secret_access_role_arn: NotRequired[
        "aws_sdk_datasync.types.iam_role_arn_or_empty_string.IamRoleArnOrEmptyString"
    ]
    """<p>Specifies the ARN for the Identity and Access Management role that DataSync uses to access the secret specified for <code>SecretArn</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomSecretConfig) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "secret_access_role_arn" in value:
        out["SecretAccessRoleArn"] = value["secret_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomSecretConfig:
    out: CustomSecretConfig = {}  # type: ignore[typeddict-item]
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    if "SecretAccessRoleArn" in data:
        out["secret_access_role_arn"] = data["SecretAccessRoleArn"]
    return out
