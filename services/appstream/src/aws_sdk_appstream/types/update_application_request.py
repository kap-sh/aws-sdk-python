"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.application_attributes
    import aws_sdk_appstream.types.arn
    import aws_sdk_appstream.types.description
    import aws_sdk_appstream.types.display_name
    import aws_sdk_appstream.types.name
    import aws_sdk_appstream.types.s3_location
    import aws_sdk_appstream.types.string


class UpdateApplicationRequest(TypedDict):
    name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the application. This name is visible to users when display name is not specified.</p>"""
    display_name: NotRequired["aws_sdk_appstream.types.display_name.DisplayName"]
    """<p>The display name of the application. This name is visible to users in the application catalog.</p>"""
    description: NotRequired["aws_sdk_appstream.types.description.Description"]
    """<p>The description of the application.</p>"""
    icon_s3_location: NotRequired["aws_sdk_appstream.types.s3_location.S3Location"]
    """<p>The icon S3 location of the application.</p>"""
    launch_path: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The launch path of the application.</p>"""
    working_directory: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The working directory of the application.</p>"""
    launch_parameters: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The launch parameters of the application.</p>"""
    app_block_arn: NotRequired["aws_sdk_appstream.types.arn.Arn"]
    """<p>The ARN of the app block.</p>"""
    attributes_to_delete: NotRequired[
        "aws_sdk_appstream.types.application_attributes.ApplicationAttributes"
    ]
    """<p>The attributes to delete for an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "icon_s3_location" in value:
        import aws_sdk_appstream.types.s3_location

        out["IconS3Location"] = (
            aws_sdk_appstream.types.s3_location.serialize_aws_json_1_1(
                value["icon_s3_location"]
            )
        )
    if "launch_path" in value:
        out["LaunchPath"] = value["launch_path"]
    if "working_directory" in value:
        out["WorkingDirectory"] = value["working_directory"]
    if "launch_parameters" in value:
        out["LaunchParameters"] = value["launch_parameters"]
    if "app_block_arn" in value:
        out["AppBlockArn"] = value["app_block_arn"]
    if "attributes_to_delete" in value:
        import aws_sdk_appstream.types.application_attributes

        out["AttributesToDelete"] = (
            aws_sdk_appstream.types.application_attributes.serialize_aws_json_1_1(
                value["attributes_to_delete"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "IconS3Location" in data:
        import aws_sdk_appstream.types.s3_location

        out["icon_s3_location"] = (
            aws_sdk_appstream.types.s3_location.deserialize_aws_json_1_1(
                data["IconS3Location"]
            )
        )
    if "LaunchPath" in data:
        out["launch_path"] = data["LaunchPath"]
    if "WorkingDirectory" in data:
        out["working_directory"] = data["WorkingDirectory"]
    if "LaunchParameters" in data:
        out["launch_parameters"] = data["LaunchParameters"]
    if "AppBlockArn" in data:
        out["app_block_arn"] = data["AppBlockArn"]
    if "AttributesToDelete" in data:
        import aws_sdk_appstream.types.application_attributes

        out["attributes_to_delete"] = (
            aws_sdk_appstream.types.application_attributes.deserialize_aws_json_1_1(
                data["AttributesToDelete"]
            )
        )
    return out
