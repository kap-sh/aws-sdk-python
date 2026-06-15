"""Generated from Smithy shape ``com.amazonaws.appconfig#UpdateAccountSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.deletion_protection_settings


class UpdateAccountSettingsRequest(TypedDict):
    deletion_protection: NotRequired[
        "aws_sdk_appconfig.types.deletion_protection_settings.DeletionProtectionSettings"
    ]
    r"""<p>A parameter to configure deletion protection. Deletion protection prevents a user from deleting a configuration profile or an environment if AppConfig has called either <a href=\"https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html\">GetLatestConfiguration</a> or for the configuration profile or from the environment during the specified interval. The default interval for <code>ProtectionPeriodInMinutes</code> is 60.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountSettingsRequest) -> dict:
    out: dict = {}
    if "deletion_protection" in value:
        import aws_sdk_appconfig.types.deletion_protection_settings

        out["DeletionProtection"] = (
            aws_sdk_appconfig.types.deletion_protection_settings.serialize_json(
                value["deletion_protection"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAccountSettingsRequest:
    out: UpdateAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    if "DeletionProtection" in data:
        import aws_sdk_appconfig.types.deletion_protection_settings

        out["deletion_protection"] = (
            aws_sdk_appconfig.types.deletion_protection_settings.deserialize_json(
                data["DeletionProtection"]
            )
        )
    return out
