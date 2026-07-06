"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PutApplicationSessionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_arn
    import aws_sdk_sso_admin.types.user_background_session_application_status


class PutApplicationSessionConfigurationRequest(TypedDict, closed=True):
    application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn"
    """<p>The Amazon Resource Name (ARN) of the application for which to update the session configuration.</p>"""
    user_background_session_application_status: NotRequired[
        "aws_sdk_sso_admin.types.user_background_session_application_status.UserBackgroundSessionApplicationStatus"
    ]
    """<p>The status of user background sessions for the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutApplicationSessionConfigurationRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    if "user_background_session_application_status" in value:
        import aws_sdk_sso_admin.types.user_background_session_application_status

        out["UserBackgroundSessionApplicationStatus"] = (
            aws_sdk_sso_admin.types.user_background_session_application_status.serialize_aws_json_1_1(
                value["user_background_session_application_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutApplicationSessionConfigurationRequest:
    out: PutApplicationSessionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "PutApplicationSessionConfigurationRequest.application_arn required"
        )
    if "UserBackgroundSessionApplicationStatus" in data:
        import aws_sdk_sso_admin.types.user_background_session_application_status

        out["user_background_session_application_status"] = (
            aws_sdk_sso_admin.types.user_background_session_application_status.deserialize_aws_json_1_1(
                data["UserBackgroundSessionApplicationStatus"]
            )
        )
    return out
