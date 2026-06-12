"""Generated from Smithy shape ``com.amazonaws.codedeploy#RegisterOnPremisesInstanceInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.iam_session_arn
    import aws_sdk_codedeploy.types.iam_user_arn
    import aws_sdk_codedeploy.types.instance_name


class RegisterOnPremisesInstanceInput(TypedDict):
    instance_name: "aws_sdk_codedeploy.types.instance_name.InstanceName"
    """<p>The name of the on-premises instance to register.</p>"""
    iam_session_arn: NotRequired[
        "aws_sdk_codedeploy.types.iam_session_arn.IamSessionArn"
    ]
    """<p>The ARN of the IAM session to associate with the on-premises instance.</p>"""
    iam_user_arn: NotRequired["aws_sdk_codedeploy.types.iam_user_arn.IamUserArn"]
    """<p>The ARN of the user to associate with the on-premises instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterOnPremisesInstanceInput) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    if "iam_session_arn" in value:
        out["iamSessionArn"] = value["iam_session_arn"]
    if "iam_user_arn" in value:
        out["iamUserArn"] = value["iam_user_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterOnPremisesInstanceInput:
    out: RegisterOnPremisesInstanceInput = {}  # type: ignore[typeddict-item]
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError(
            "RegisterOnPremisesInstanceInput.instance_name required"
        )
    if "iamSessionArn" in data:
        out["iam_session_arn"] = data["iamSessionArn"]
    if "iamUserArn" in data:
        out["iam_user_arn"] = data["iamUserArn"]
    return out
