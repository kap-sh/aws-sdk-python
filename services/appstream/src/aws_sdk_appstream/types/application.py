"""Generated from Smithy shape ``com.amazonaws.appstream#Application``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.arn
    import aws_sdk_appstream.types.boolean
    import aws_sdk_appstream.types.metadata
    import aws_sdk_appstream.types.platforms
    import aws_sdk_appstream.types.s3_location
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.string_list
    import aws_sdk_appstream.types.timestamp


class Application(TypedDict):
    name: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The name of the application.</p>"""
    display_name: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The application name to display.</p>"""
    icon_url: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The URL for the application icon. This URL might be time-limited.</p>"""
    launch_path: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The path to the application executable in the instance.</p>"""
    launch_parameters: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The arguments that are passed to the application at launch.</p>"""
    enabled: NotRequired["aws_sdk_appstream.types.boolean.Boolean"]
    """<p>If there is a problem, the application can be disabled after image creation.</p>"""
    metadata: NotRequired["aws_sdk_appstream.types.metadata.Metadata"]
    """<p>Additional attributes that describe the application.</p>"""
    working_directory: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The working directory for the application.</p>"""
    description: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The description of the application.</p>"""
    arn: NotRequired["aws_sdk_appstream.types.arn.Arn"]
    """<p>The ARN of the application.</p>"""
    app_block_arn: NotRequired["aws_sdk_appstream.types.arn.Arn"]
    """<p>The app block ARN of the application.</p>"""
    icon_s3_location: NotRequired["aws_sdk_appstream.types.s3_location.S3Location"]
    """<p>The S3 location of the application icon.</p>"""
    platforms: NotRequired["aws_sdk_appstream.types.platforms.Platforms"]
    """<p>The platforms on which the application can run.</p>"""
    instance_families: NotRequired["aws_sdk_appstream.types.string_list.StringList"]
    """<p>The instance families for the application.</p>"""
    created_time: NotRequired["aws_sdk_appstream.types.timestamp.Timestamp"]
    """<p>The time at which the application was created within the app block.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Application) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "icon_url" in value:
        out["IconURL"] = value["icon_url"]
    if "launch_path" in value:
        out["LaunchPath"] = value["launch_path"]
    if "launch_parameters" in value:
        out["LaunchParameters"] = value["launch_parameters"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "metadata" in value:
        import aws_sdk_appstream.types.metadata

        out["Metadata"] = aws_sdk_appstream.types.metadata.serialize_aws_json_1_1(
            value["metadata"]
        )
    if "working_directory" in value:
        out["WorkingDirectory"] = value["working_directory"]
    if "description" in value:
        out["Description"] = value["description"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "app_block_arn" in value:
        out["AppBlockArn"] = value["app_block_arn"]
    if "icon_s3_location" in value:
        import aws_sdk_appstream.types.s3_location

        out["IconS3Location"] = (
            aws_sdk_appstream.types.s3_location.serialize_aws_json_1_1(
                value["icon_s3_location"]
            )
        )
    if "platforms" in value:
        import aws_sdk_appstream.types.platforms

        out["Platforms"] = aws_sdk_appstream.types.platforms.serialize_aws_json_1_1(
            value["platforms"]
        )
    if "instance_families" in value:
        import aws_sdk_appstream.types.string_list

        out["InstanceFamilies"] = (
            aws_sdk_appstream.types.string_list.serialize_aws_json_1_1(
                value["instance_families"]
            )
        )
    if "created_time" in value:
        import aws_sdk_appstream.types.timestamp

        out["CreatedTime"] = aws_sdk_appstream.types.timestamp.serialize_aws_json_1_1(
            value["created_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Application:
    out: Application = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "IconURL" in data:
        out["icon_url"] = data["IconURL"]
    if "LaunchPath" in data:
        out["launch_path"] = data["LaunchPath"]
    if "LaunchParameters" in data:
        out["launch_parameters"] = data["LaunchParameters"]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "Metadata" in data:
        import aws_sdk_appstream.types.metadata

        out["metadata"] = aws_sdk_appstream.types.metadata.deserialize_aws_json_1_1(
            data["Metadata"]
        )
    if "WorkingDirectory" in data:
        out["working_directory"] = data["WorkingDirectory"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AppBlockArn" in data:
        out["app_block_arn"] = data["AppBlockArn"]
    if "IconS3Location" in data:
        import aws_sdk_appstream.types.s3_location

        out["icon_s3_location"] = (
            aws_sdk_appstream.types.s3_location.deserialize_aws_json_1_1(
                data["IconS3Location"]
            )
        )
    if "Platforms" in data:
        import aws_sdk_appstream.types.platforms

        out["platforms"] = aws_sdk_appstream.types.platforms.deserialize_aws_json_1_1(
            data["Platforms"]
        )
    if "InstanceFamilies" in data:
        import aws_sdk_appstream.types.string_list

        out["instance_families"] = (
            aws_sdk_appstream.types.string_list.deserialize_aws_json_1_1(
                data["InstanceFamilies"]
            )
        )
    if "CreatedTime" in data:
        import aws_sdk_appstream.types.timestamp

        out["created_time"] = (
            aws_sdk_appstream.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    return out
