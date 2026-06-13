"""Generated from Smithy shape ``com.amazonaws.s3files#GetAccessPointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3files.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3files.types.access_point_arn
    import aws_sdk_s3files.types.access_point_id
    import aws_sdk_s3files.types.aws_account_id
    import aws_sdk_s3files.types.client_token
    import aws_sdk_s3files.types.file_system_id
    import aws_sdk_s3files.types.life_cycle_state
    import aws_sdk_s3files.types.posix_user
    import aws_sdk_s3files.types.root_directory
    import aws_sdk_s3files.types.tag_list
    import aws_sdk_s3files.types.tag_value


class GetAccessPointResponse(TypedDict):
    access_point_arn: "aws_sdk_s3files.types.access_point_arn.AccessPointArn"
    """<p>The ARN of the access point.</p>"""
    access_point_id: "aws_sdk_s3files.types.access_point_id.AccessPointId"
    """<p>The ID of the access point.</p>"""
    client_token: "aws_sdk_s3files.types.client_token.ClientToken"
    """<p>The client token used for idempotency when the access point was created.</p>"""
    file_system_id: "aws_sdk_s3files.types.file_system_id.FileSystemId"
    """<p>The ID of the S3 File System.</p>"""
    status: "aws_sdk_s3files.types.life_cycle_state.LifeCycleState"
    """<p>The current status of the access point.</p>"""
    owner_id: "aws_sdk_s3files.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID of the access point owner.</p>"""
    posix_user: NotRequired["aws_sdk_s3files.types.posix_user.PosixUser"]
    """<p>The POSIX identity configured for this access point.</p>"""
    root_directory: NotRequired["aws_sdk_s3files.types.root_directory.RootDirectory"]
    """<p>The root directory configuration for this access point.</p>"""
    tags: NotRequired["aws_sdk_s3files.types.tag_list.TagList"]
    """<p>The tags associated with the access point.</p>"""
    name: NotRequired["aws_sdk_s3files.types.tag_value.TagValue"]
    """<p>The name of the access point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessPointResponse) -> dict:
    out: dict = {}
    out["accessPointArn"] = value["access_point_arn"]
    out["accessPointId"] = value["access_point_id"]
    out["clientToken"] = value["client_token"]
    out["fileSystemId"] = value["file_system_id"]
    import aws_sdk_s3files.types.life_cycle_state

    out["status"] = aws_sdk_s3files.types.life_cycle_state.serialize_json(
        value["status"]
    )
    out["ownerId"] = value["owner_id"]
    if "posix_user" in value:
        import aws_sdk_s3files.types.posix_user

        out["posixUser"] = aws_sdk_s3files.types.posix_user.serialize_json(
            value["posix_user"]
        )
    if "root_directory" in value:
        import aws_sdk_s3files.types.root_directory

        out["rootDirectory"] = aws_sdk_s3files.types.root_directory.serialize_json(
            value["root_directory"]
        )
    if "tags" in value:
        import aws_sdk_s3files.types.tag_list

        out["tags"] = aws_sdk_s3files.types.tag_list.serialize_json(value["tags"])
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> GetAccessPointResponse:
    out: GetAccessPointResponse = {}  # type: ignore[typeddict-item]
    if "accessPointArn" in data:
        out["access_point_arn"] = data["accessPointArn"]
    else:
        raise DeserializationError("GetAccessPointResponse.access_point_arn required")
    if "accessPointId" in data:
        out["access_point_id"] = data["accessPointId"]
    else:
        raise DeserializationError("GetAccessPointResponse.access_point_id required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("GetAccessPointResponse.client_token required")
    if "fileSystemId" in data:
        out["file_system_id"] = data["fileSystemId"]
    else:
        raise DeserializationError("GetAccessPointResponse.file_system_id required")
    if "status" in data:
        import aws_sdk_s3files.types.life_cycle_state

        out["status"] = aws_sdk_s3files.types.life_cycle_state.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetAccessPointResponse.status required")
    if "ownerId" in data:
        out["owner_id"] = data["ownerId"]
    else:
        raise DeserializationError("GetAccessPointResponse.owner_id required")
    if "posixUser" in data:
        import aws_sdk_s3files.types.posix_user

        out["posix_user"] = aws_sdk_s3files.types.posix_user.deserialize_json(
            data["posixUser"]
        )
    if "rootDirectory" in data:
        import aws_sdk_s3files.types.root_directory

        out["root_directory"] = aws_sdk_s3files.types.root_directory.deserialize_json(
            data["rootDirectory"]
        )
    if "tags" in data:
        import aws_sdk_s3files.types.tag_list

        out["tags"] = aws_sdk_s3files.types.tag_list.deserialize_json(data["tags"])
    if "name" in data:
        out["name"] = data["name"]
    return out
