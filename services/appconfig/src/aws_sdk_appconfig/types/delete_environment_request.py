"""Generated from Smithy shape ``com.amazonaws.appconfig#DeleteEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.deletion_protection_check
    import aws_sdk_appconfig.types.id


class DeleteEnvironmentRequest(TypedDict):
    environment_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The ID of the environment that you want to delete.</p>"""
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The application ID that includes the environment that you want to delete.</p>"""
    deletion_protection_check: NotRequired[
        "aws_sdk_appconfig.types.deletion_protection_check.DeletionProtectionCheck"
    ]
    """<p>A parameter to configure deletion protection. Deletion protection prevents a user from deleting an environment if your application called either <a href=\"https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html\">GetLatestConfiguration</a> or in the environment during the specified interval. </p> <p>This parameter supports the following values:</p> <ul> <li> <p> <code>BYPASS</code>: Instructs AppConfig to bypass the deletion protection check and delete a configuration profile even if deletion protection would have otherwise prevented it. </p> </li> <li> <p> <code>APPLY</code>: Instructs the deletion protection check to run, even if deletion protection is disabled at the account level. <code>APPLY</code> also forces the deletion protection check to run against resources created in the past hour, which are normally excluded from deletion protection checks.</p> </li> <li> <p> <code>ACCOUNT_DEFAULT</code>: The default setting, which instructs AppConfig to implement the deletion protection value specified in the <code>UpdateAccountSettings</code> API.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEnvironmentRequest:
    out: DeleteEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
