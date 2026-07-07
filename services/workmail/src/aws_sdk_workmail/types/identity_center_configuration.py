"""Generated from Smithy shape ``com.amazonaws.workmail#IdentityCenterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.application_arn
    import aws_sdk_workmail.types.instance_arn


class IdentityCenterConfiguration(TypedDict, closed=True):
    instance_arn: "aws_sdk_workmail.types.instance_arn.InstanceArn"
    """<p> The Amazon Resource Name (ARN) of the of IAM Identity Center instance. Must be in the same AWS account and region as WorkMail organization.</p>"""
    application_arn: "aws_sdk_workmail.types.application_arn.ApplicationArn"
    """<p> The Amazon Resource Name (ARN) of IAMIdentity Center Application for WorkMail. Must be created by the WorkMail API, see CreateIdentityCenterApplication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityCenterConfiguration) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityCenterConfiguration:
    out: IdentityCenterConfiguration = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError("IdentityCenterConfiguration.instance_arn required")
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "IdentityCenterConfiguration.application_arn required"
        )
    return out
