"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateBuildOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.aws_credentials
    import aws_sdk_gamelift.types.build
    import aws_sdk_gamelift.types.s3_location


class CreateBuildOutput(TypedDict):
    build: NotRequired["aws_sdk_gamelift.types.build.Build"]
    """<p>The newly created build resource, including a unique build IDs and status. </p>"""
    upload_credentials: NotRequired[
        "aws_sdk_gamelift.types.aws_credentials.AwsCredentials"
    ]
    r"""<p>This element is returned only when the operation is called without a storage location. It contains credentials to use when you are uploading a build file to an Amazon S3 bucket that is owned by Amazon GameLift Servers. Credentials have a limited life span. To refresh these credentials, call <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_RequestUploadCredentials.html\">RequestUploadCredentials</a>. </p>"""
    storage_location: NotRequired["aws_sdk_gamelift.types.s3_location.S3Location"]
    """<p>Amazon S3 location for your game build file, including bucket name and key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBuildOutput) -> dict:
    out: dict = {}
    if "build" in value:
        import aws_sdk_gamelift.types.build

        out["Build"] = aws_sdk_gamelift.types.build.serialize_aws_json_1_1(
            value["build"]
        )
    if "upload_credentials" in value:
        import aws_sdk_gamelift.types.aws_credentials

        out["UploadCredentials"] = (
            aws_sdk_gamelift.types.aws_credentials.serialize_aws_json_1_1(
                value["upload_credentials"]
            )
        )
    if "storage_location" in value:
        import aws_sdk_gamelift.types.s3_location

        out["StorageLocation"] = (
            aws_sdk_gamelift.types.s3_location.serialize_aws_json_1_1(
                value["storage_location"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBuildOutput:
    out: CreateBuildOutput = {}  # type: ignore[typeddict-item]
    if "Build" in data:
        import aws_sdk_gamelift.types.build

        out["build"] = aws_sdk_gamelift.types.build.deserialize_aws_json_1_1(
            data["Build"]
        )
    if "UploadCredentials" in data:
        import aws_sdk_gamelift.types.aws_credentials

        out["upload_credentials"] = (
            aws_sdk_gamelift.types.aws_credentials.deserialize_aws_json_1_1(
                data["UploadCredentials"]
            )
        )
    if "StorageLocation" in data:
        import aws_sdk_gamelift.types.s3_location

        out["storage_location"] = (
            aws_sdk_gamelift.types.s3_location.deserialize_aws_json_1_1(
                data["StorageLocation"]
            )
        )
    return out
