"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DataProtectionSettingsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.description_safe
    import aws_sdk_workspaces_web.types.display_name_safe
    import aws_sdk_workspaces_web.types.timestamp


class DataProtectionSettingsSummary(TypedDict, closed=True):
    data_protection_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the data protection settings.</p>"""
    display_name: NotRequired[
        "aws_sdk_workspaces_web.types.display_name_safe.DisplayNameSafe"
    ]
    """<p>The display name of the data protection settings.</p>"""
    description: NotRequired[
        "aws_sdk_workspaces_web.types.description_safe.DescriptionSafe"
    ]
    """<p>The description of the data protection settings.</p>"""
    creation_date: NotRequired["aws_sdk_workspaces_web.types.timestamp.Timestamp"]
    """<p>The creation date timestamp of the data protection settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProtectionSettingsSummary) -> dict:
    out: dict = {}
    out["dataProtectionSettingsArn"] = value["data_protection_settings_arn"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "creation_date" in value:
        import aws_sdk_workspaces_web.types.timestamp

        out["creationDate"] = aws_sdk_workspaces_web.types.timestamp.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> DataProtectionSettingsSummary:
    out: DataProtectionSettingsSummary = {}  # type: ignore[typeddict-item]
    if "dataProtectionSettingsArn" in data:
        out["data_protection_settings_arn"] = data["dataProtectionSettingsArn"]
    else:
        raise DeserializationError(
            "DataProtectionSettingsSummary.data_protection_settings_arn required"
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "creationDate" in data:
        import aws_sdk_workspaces_web.types.timestamp

        out["creation_date"] = aws_sdk_workspaces_web.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    return out
