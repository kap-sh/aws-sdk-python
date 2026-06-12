"""Generated from Smithy shape ``com.amazonaws.gamelift#Build``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.build_arn
    import aws_sdk_gamelift.types.build_id
    import aws_sdk_gamelift.types.build_status
    import aws_sdk_gamelift.types.free_text
    import aws_sdk_gamelift.types.operating_system
    import aws_sdk_gamelift.types.server_sdk_version
    import aws_sdk_gamelift.types.timestamp
    import aws_sdk_gamelift.types.whole_number_long


class Build(TypedDict):
    build_id: NotRequired["aws_sdk_gamelift.types.build_id.BuildId"]
    """<p>A unique identifier for the build.</p>"""
    build_arn: NotRequired["aws_sdk_gamelift.types.build_arn.BuildArn"]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html\">ARN</a>) that is assigned to a Amazon GameLift Servers build resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::build/build-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>. In a GameLift build ARN, the resource ID matches the <i>BuildId</i> value.</p>"""
    name: NotRequired["aws_sdk_gamelift.types.free_text.FreeText"]
    """<p>A descriptive label that is associated with a build. Build names do not need to be unique. It can be set using <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateBuild.html\">CreateBuild</a> or <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/UpdateBuild\">UpdateBuild</a>.</p>"""
    version: NotRequired["aws_sdk_gamelift.types.free_text.FreeText"]
    """<p>Version information that is associated with a build or script. Version strings do not need to be unique.</p>"""
    status: NotRequired["aws_sdk_gamelift.types.build_status.BuildStatus"]
    """<p>Current status of the build.</p> <p>Possible build statuses include the following:</p> <ul> <li> <p> <b>INITIALIZED</b> -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value. </p> </li> <li> <p> <b>READY</b> -- The game build has been successfully uploaded. You can now create new fleets for this build.</p> </li> <li> <p> <b>FAILED</b> -- The game build upload failed. You cannot create new fleets for this build. </p> </li> </ul>"""
    size_on_disk: NotRequired[
        "aws_sdk_gamelift.types.whole_number_long.WholeNumberLong"
    ]
    """<p>File size of the uploaded game build, expressed in bytes. When the build status is <code>INITIALIZED</code> or when using a custom Amazon S3 storage location, this value is 0.</p>"""
    operating_system: NotRequired[
        "aws_sdk_gamelift.types.operating_system.OperatingSystem"
    ]
    """<p>Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build.</p> <note> <p>Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the <a href=\"http://aws.amazon.com/amazon-linux-2/faqs/\">Amazon Linux 2 FAQs</a>. For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See <a href=\"https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html\"> Migrate to server SDK version 5.</a> </p> </note>"""
    creation_time: NotRequired["aws_sdk_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example <code>\"1469498468.057\"</code>).</p>"""
    server_sdk_version: NotRequired[
        "aws_sdk_gamelift.types.server_sdk_version.ServerSdkVersion"
    ]
    """<p>The Amazon GameLift Servers Server SDK version used to develop your game server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Build) -> dict:
    out: dict = {}
    if "build_id" in value:
        out["BuildId"] = value["build_id"]
    if "build_arn" in value:
        out["BuildArn"] = value["build_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    if "status" in value:
        import aws_sdk_gamelift.types.build_status

        out["Status"] = aws_sdk_gamelift.types.build_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "size_on_disk" in value:
        out["SizeOnDisk"] = value["size_on_disk"]
    if "operating_system" in value:
        import aws_sdk_gamelift.types.operating_system

        out["OperatingSystem"] = (
            aws_sdk_gamelift.types.operating_system.serialize_aws_json_1_1(
                value["operating_system"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_gamelift.types.timestamp

        out["CreationTime"] = aws_sdk_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "server_sdk_version" in value:
        out["ServerSdkVersion"] = value["server_sdk_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Build:
    out: Build = {}  # type: ignore[typeddict-item]
    if "BuildId" in data:
        out["build_id"] = data["BuildId"]
    if "BuildArn" in data:
        out["build_arn"] = data["BuildArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Status" in data:
        import aws_sdk_gamelift.types.build_status

        out["status"] = aws_sdk_gamelift.types.build_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "SizeOnDisk" in data:
        out["size_on_disk"] = data["SizeOnDisk"]
    if "OperatingSystem" in data:
        import aws_sdk_gamelift.types.operating_system

        out["operating_system"] = (
            aws_sdk_gamelift.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_gamelift.types.timestamp

        out["creation_time"] = (
            aws_sdk_gamelift.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "ServerSdkVersion" in data:
        out["server_sdk_version"] = data["ServerSdkVersion"]
    return out
