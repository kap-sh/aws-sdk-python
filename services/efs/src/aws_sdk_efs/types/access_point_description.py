"""Generated from Smithy shape ``com.amazonaws.efs#AccessPointDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.access_point_arn
    import aws_sdk_efs.types.access_point_id
    import aws_sdk_efs.types.aws_account_id
    import aws_sdk_efs.types.client_token
    import aws_sdk_efs.types.file_system_id
    import aws_sdk_efs.types.life_cycle_state
    import aws_sdk_efs.types.name
    import aws_sdk_efs.types.posix_user
    import aws_sdk_efs.types.root_directory
    import aws_sdk_efs.types.tags


class AccessPointDescription(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_efs.types.client_token.ClientToken"]
    """<p>The opaque string specified in the request to ensure idempotent creation.</p>"""
    name: NotRequired["aws_sdk_efs.types.name.Name"]
    """<p>The name of the access point. This is the value of the <code>Name</code> tag.</p>"""
    tags: NotRequired["aws_sdk_efs.types.tags.Tags"]
    """<p>The tags associated with the access point, presented as an array of Tag objects.</p>"""
    access_point_id: NotRequired["aws_sdk_efs.types.access_point_id.AccessPointId"]
    """<p>The ID of the access point, assigned by Amazon EFS.</p>"""
    access_point_arn: NotRequired["aws_sdk_efs.types.access_point_arn.AccessPointArn"]
    """<p>The unique Amazon Resource Name (ARN) associated with the access point.</p>"""
    file_system_id: NotRequired["aws_sdk_efs.types.file_system_id.FileSystemId"]
    """<p>The ID of the EFS file system that the access point applies to.</p>"""
    posix_user: NotRequired["aws_sdk_efs.types.posix_user.PosixUser"]
    """<p>The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by NFS clients using the access point.</p>"""
    root_directory: NotRequired["aws_sdk_efs.types.root_directory.RootDirectory"]
    """<p>The directory on the EFS file system that the access point exposes as the root directory to NFS clients using the access point.</p>"""
    owner_id: NotRequired["aws_sdk_efs.types.aws_account_id.AwsAccountId"]
    """<p>Identifies the Amazon Web Services account that owns the access point resource.</p>"""
    life_cycle_state: NotRequired["aws_sdk_efs.types.life_cycle_state.LifeCycleState"]
    """<p>Identifies the lifecycle phase of the access point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessPointDescription) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "name" in value:
        out["Name"] = value["name"]
    if "tags" in value:
        import aws_sdk_efs.types.tags

        out["Tags"] = aws_sdk_efs.types.tags.serialize_json(value["tags"])
    if "access_point_id" in value:
        out["AccessPointId"] = value["access_point_id"]
    if "access_point_arn" in value:
        out["AccessPointArn"] = value["access_point_arn"]
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "posix_user" in value:
        import aws_sdk_efs.types.posix_user

        out["PosixUser"] = aws_sdk_efs.types.posix_user.serialize_json(
            value["posix_user"]
        )
    if "root_directory" in value:
        import aws_sdk_efs.types.root_directory

        out["RootDirectory"] = aws_sdk_efs.types.root_directory.serialize_json(
            value["root_directory"]
        )
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "life_cycle_state" in value:
        import aws_sdk_efs.types.life_cycle_state

        out["LifeCycleState"] = aws_sdk_efs.types.life_cycle_state.serialize_json(
            value["life_cycle_state"]
        )
    return out


def deserialize_json(data: dict) -> AccessPointDescription:
    out: AccessPointDescription = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Tags" in data:
        import aws_sdk_efs.types.tags

        out["tags"] = aws_sdk_efs.types.tags.deserialize_json(data["Tags"])
    if "AccessPointId" in data:
        out["access_point_id"] = data["AccessPointId"]
    if "AccessPointArn" in data:
        out["access_point_arn"] = data["AccessPointArn"]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "PosixUser" in data:
        import aws_sdk_efs.types.posix_user

        out["posix_user"] = aws_sdk_efs.types.posix_user.deserialize_json(
            data["PosixUser"]
        )
    if "RootDirectory" in data:
        import aws_sdk_efs.types.root_directory

        out["root_directory"] = aws_sdk_efs.types.root_directory.deserialize_json(
            data["RootDirectory"]
        )
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "LifeCycleState" in data:
        import aws_sdk_efs.types.life_cycle_state

        out["life_cycle_state"] = aws_sdk_efs.types.life_cycle_state.deserialize_json(
            data["LifeCycleState"]
        )
    return out
