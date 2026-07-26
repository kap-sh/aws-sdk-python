"""Generated from Smithy shape ``com.amazonaws.s3files#ListAccessPointsDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3files.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3files.types.access_point_arn
    import capo_s3files.types.access_point_id
    import capo_s3files.types.aws_account_id
    import capo_s3files.types.file_system_id
    import capo_s3files.types.life_cycle_state
    import capo_s3files.types.posix_user
    import capo_s3files.types.root_directory
    import capo_s3files.types.tag_value


class ListAccessPointsDescription(TypedDict, closed=True):
    access_point_arn: "capo_s3files.types.access_point_arn.AccessPointArn"
    """<p>The Amazon Resource Name (ARN) of the access point.</p>"""
    access_point_id: "capo_s3files.types.access_point_id.AccessPointId"
    """<p>The ID of the access point.</p>"""
    file_system_id: "capo_s3files.types.file_system_id.FileSystemId"
    """<p>The ID of the S3 File System.</p>"""
    status: "capo_s3files.types.life_cycle_state.LifeCycleState"
    """<p>The current status of the access point.</p>"""
    owner_id: "capo_s3files.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID of the access point owner.</p>"""
    posix_user: NotRequired["capo_s3files.types.posix_user.PosixUser"]
    """<p>The POSIX identity configured for this access point.</p>"""
    root_directory: NotRequired["capo_s3files.types.root_directory.RootDirectory"]
    """<p>The root directory configuration for this access point.</p>"""
    name: NotRequired["capo_s3files.types.tag_value.TagValue"]
    """<p>The name of the access point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessPointsDescription) -> dict:
    out: dict = {}
    out["accessPointArn"] = value["access_point_arn"]
    out["accessPointId"] = value["access_point_id"]
    out["fileSystemId"] = value["file_system_id"]
    import capo_s3files.types.life_cycle_state

    out["status"] = capo_s3files.types.life_cycle_state.serialize_json(value["status"])
    out["ownerId"] = value["owner_id"]
    if "posix_user" in value:
        import capo_s3files.types.posix_user

        out["posixUser"] = capo_s3files.types.posix_user.serialize_json(
            value["posix_user"]
        )
    if "root_directory" in value:
        import capo_s3files.types.root_directory

        out["rootDirectory"] = capo_s3files.types.root_directory.serialize_json(
            value["root_directory"]
        )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ListAccessPointsDescription:
    out: ListAccessPointsDescription = {}  # type: ignore[typeddict-item]
    if "accessPointArn" in data:
        out["access_point_arn"] = data["accessPointArn"]
    else:
        raise DeserializationError(
            "ListAccessPointsDescription.access_point_arn required"
        )
    if "accessPointId" in data:
        out["access_point_id"] = data["accessPointId"]
    else:
        raise DeserializationError(
            "ListAccessPointsDescription.access_point_id required"
        )
    if "fileSystemId" in data:
        out["file_system_id"] = data["fileSystemId"]
    else:
        raise DeserializationError(
            "ListAccessPointsDescription.file_system_id required"
        )
    if "status" in data:
        import capo_s3files.types.life_cycle_state

        out["status"] = capo_s3files.types.life_cycle_state.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ListAccessPointsDescription.status required")
    if "ownerId" in data:
        out["owner_id"] = data["ownerId"]
    else:
        raise DeserializationError("ListAccessPointsDescription.owner_id required")
    if "posixUser" in data:
        import capo_s3files.types.posix_user

        out["posix_user"] = capo_s3files.types.posix_user.deserialize_json(
            data["posixUser"]
        )
    if "rootDirectory" in data:
        import capo_s3files.types.root_directory

        out["root_directory"] = capo_s3files.types.root_directory.deserialize_json(
            data["rootDirectory"]
        )
    if "name" in data:
        out["name"] = data["name"]
    return out
