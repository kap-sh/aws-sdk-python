"""Generated from Smithy shape ``com.amazonaws.appstream#AgentAccessConfigForUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.agent_access_setting_list
    import aws_sdk_appstream.types.boolean_object
    import aws_sdk_appstream.types.s3_bucket_arn
    import aws_sdk_appstream.types.screen_image_format
    import aws_sdk_appstream.types.screen_resolution


class AgentAccessConfigForUpdate(TypedDict, closed=True):
    settings: NotRequired[
        "aws_sdk_appstream.types.agent_access_setting_list.AgentAccessSettingList"
    ]
    """<p>The list of agent access settings that define permissions for each agent action.</p>"""
    s3_bucket_arn: NotRequired["aws_sdk_appstream.types.s3_bucket_arn.S3BucketArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon S3 bucket where agent screenshots are stored.</p>"""
    screenshots_upload_enabled: NotRequired[
        "aws_sdk_appstream.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether screenshot uploads to Amazon S3 are enabled for agent sessions.</p>"""
    screen_resolution: NotRequired[
        "aws_sdk_appstream.types.screen_resolution.ScreenResolution"
    ]
    """<p>The screen resolution for the agent streaming environment.</p>"""
    screen_image_format: NotRequired[
        "aws_sdk_appstream.types.screen_image_format.ScreenImageFormat"
    ]
    """<p>The image format for agent screen captures.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentAccessConfigForUpdate) -> dict:
    out: dict = {}
    if "settings" in value:
        import aws_sdk_appstream.types.agent_access_setting_list

        out["Settings"] = (
            aws_sdk_appstream.types.agent_access_setting_list.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "s3_bucket_arn" in value:
        out["S3BucketArn"] = value["s3_bucket_arn"]
    if "screenshots_upload_enabled" in value:
        out["ScreenshotsUploadEnabled"] = value["screenshots_upload_enabled"]
    if "screen_resolution" in value:
        import aws_sdk_appstream.types.screen_resolution

        out["ScreenResolution"] = (
            aws_sdk_appstream.types.screen_resolution.serialize_aws_json_1_1(
                value["screen_resolution"]
            )
        )
    if "screen_image_format" in value:
        import aws_sdk_appstream.types.screen_image_format

        out["ScreenImageFormat"] = (
            aws_sdk_appstream.types.screen_image_format.serialize_aws_json_1_1(
                value["screen_image_format"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentAccessConfigForUpdate:
    out: AgentAccessConfigForUpdate = {}  # type: ignore[typeddict-item]
    if "Settings" in data:
        import aws_sdk_appstream.types.agent_access_setting_list

        out["settings"] = (
            aws_sdk_appstream.types.agent_access_setting_list.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    if "S3BucketArn" in data:
        out["s3_bucket_arn"] = data["S3BucketArn"]
    if "ScreenshotsUploadEnabled" in data:
        out["screenshots_upload_enabled"] = data["ScreenshotsUploadEnabled"]
    if "ScreenResolution" in data:
        import aws_sdk_appstream.types.screen_resolution

        out["screen_resolution"] = (
            aws_sdk_appstream.types.screen_resolution.deserialize_aws_json_1_1(
                data["ScreenResolution"]
            )
        )
    if "ScreenImageFormat" in data:
        import aws_sdk_appstream.types.screen_image_format

        out["screen_image_format"] = (
            aws_sdk_appstream.types.screen_image_format.deserialize_aws_json_1_1(
                data["ScreenImageFormat"]
            )
        )
    return out
