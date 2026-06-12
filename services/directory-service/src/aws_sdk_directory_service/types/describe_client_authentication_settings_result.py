"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeClientAuthenticationSettingsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.client_authentication_settings_info
    import aws_sdk_directory_service.types.next_token


class DescribeClientAuthenticationSettingsResult(TypedDict):
    client_authentication_settings_info: NotRequired[
        "aws_sdk_directory_service.types.client_authentication_settings_info.ClientAuthenticationSettingsInfo"
    ]
    """<p>Information about the type of client authentication for the specified directory. The following information is retrieved: The date and time when the status of the client authentication type was last updated, whether the client authentication type is enabled or disabled, and the type of client authentication.</p>"""
    next_token: NotRequired["aws_sdk_directory_service.types.next_token.NextToken"]
    """<p>The next token used to retrieve the client authentication settings if the number of setting types exceeds page limit and there is another page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClientAuthenticationSettingsResult) -> dict:
    out: dict = {}
    if "client_authentication_settings_info" in value:
        import aws_sdk_directory_service.types.client_authentication_settings_info

        out["ClientAuthenticationSettingsInfo"] = (
            aws_sdk_directory_service.types.client_authentication_settings_info.serialize_aws_json_1_1(
                value["client_authentication_settings_info"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClientAuthenticationSettingsResult:
    out: DescribeClientAuthenticationSettingsResult = {}  # type: ignore[typeddict-item]
    if "ClientAuthenticationSettingsInfo" in data:
        import aws_sdk_directory_service.types.client_authentication_settings_info

        out["client_authentication_settings_info"] = (
            aws_sdk_directory_service.types.client_authentication_settings_info.deserialize_aws_json_1_1(
                data["ClientAuthenticationSettingsInfo"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
