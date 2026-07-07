"""Generated from Smithy shape ``com.amazonaws.cognitosync#PushSync``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.application_arn_list
    import aws_sdk_cognito_sync.types.assume_role_arn


class PushSync(TypedDict, closed=True):
    application_arns: NotRequired[
        "aws_sdk_cognito_sync.types.application_arn_list.ApplicationArnList"
    ]
    """<p>List of SNS platform application ARNs that could be used by clients.</p>"""
    role_arn: NotRequired["aws_sdk_cognito_sync.types.assume_role_arn.AssumeRoleArn"]
    """<p>A role configured to allow Cognito to call SNS on behalf of the developer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PushSync) -> dict:
    out: dict = {}
    if "application_arns" in value:
        import aws_sdk_cognito_sync.types.application_arn_list

        out["ApplicationArns"] = (
            aws_sdk_cognito_sync.types.application_arn_list.serialize_json(
                value["application_arns"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> PushSync:
    out: PushSync = {}  # type: ignore[typeddict-item]
    if "ApplicationArns" in data:
        import aws_sdk_cognito_sync.types.application_arn_list

        out["application_arns"] = (
            aws_sdk_cognito_sync.types.application_arn_list.deserialize_json(
                data["ApplicationArns"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
