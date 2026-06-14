"""Generated from Smithy shape ``com.amazonaws.workspaces#ApplicationSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.application_settings_status_enum
    import aws_sdk_workspaces.types.s3_bucket_name
    import aws_sdk_workspaces.types.settings_group


class ApplicationSettingsResponse(TypedDict):
    status: "aws_sdk_workspaces.types.application_settings_status_enum.ApplicationSettingsStatusEnum"
    """<p>Specifies whether persistent application settings are enabled for users during their pool sessions.</p>"""
    settings_group: NotRequired["aws_sdk_workspaces.types.settings_group.SettingsGroup"]
    """<p>The path prefix for the S3 bucket where users’ persistent application settings are stored.</p>"""
    s3_bucket_name: NotRequired["aws_sdk_workspaces.types.s3_bucket_name.S3BucketName"]
    """<p>The S3 bucket where users’ persistent application settings are stored. When persistent application settings are enabled for the first time for an account in an Amazon Web Services Region, an S3 bucket is created. The bucket is unique to the Amazon Web Services account and the Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSettingsResponse) -> dict:
    out: dict = {}
    import aws_sdk_workspaces.types.application_settings_status_enum

    out["Status"] = (
        aws_sdk_workspaces.types.application_settings_status_enum.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "settings_group" in value:
        out["SettingsGroup"] = value["settings_group"]
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSettingsResponse:
    out: ApplicationSettingsResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_workspaces.types.application_settings_status_enum

        out["status"] = (
            aws_sdk_workspaces.types.application_settings_status_enum.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("ApplicationSettingsResponse.status required")
    if "SettingsGroup" in data:
        out["settings_group"] = data["SettingsGroup"]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    return out
