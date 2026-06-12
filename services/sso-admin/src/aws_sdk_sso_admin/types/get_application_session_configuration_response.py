"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GetApplicationSessionConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.user_background_session_application_status


class GetApplicationSessionConfigurationResponse(TypedDict):
    user_background_session_application_status: NotRequired[
        "aws_sdk_sso_admin.types.user_background_session_application_status.UserBackgroundSessionApplicationStatus"
    ]
    """<p>The status of user background sessions for the application. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApplicationSessionConfigurationResponse) -> dict:
    out: dict = {}
    if "user_background_session_application_status" in value:
        import aws_sdk_sso_admin.types.user_background_session_application_status

        out["UserBackgroundSessionApplicationStatus"] = (
            aws_sdk_sso_admin.types.user_background_session_application_status.serialize_aws_json_1_1(
                value["user_background_session_application_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApplicationSessionConfigurationResponse:
    out: GetApplicationSessionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "UserBackgroundSessionApplicationStatus" in data:
        import aws_sdk_sso_admin.types.user_background_session_application_status

        out["user_background_session_application_status"] = (
            aws_sdk_sso_admin.types.user_background_session_application_status.deserialize_aws_json_1_1(
                data["UserBackgroundSessionApplicationStatus"]
            )
        )
    return out
