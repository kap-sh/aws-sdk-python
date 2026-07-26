"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEfsAccessPointDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_efs_access_point_posix_user_details
    import capo_securityhub.types.aws_efs_access_point_root_directory_details
    import capo_securityhub.types.non_empty_string


class AwsEfsAccessPointDetails(TypedDict, closed=True):
    access_point_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the Amazon EFS access point. </p>"""
    arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the Amazon EFS access point. </p>"""
    client_token: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The opaque string specified in the request to ensure idempotent creation. </p>"""
    file_system_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the Amazon EFS file system that the access point applies to. </p>"""
    posix_user: NotRequired[
        "capo_securityhub.types.aws_efs_access_point_posix_user_details.AwsEfsAccessPointPosixUserDetails"
    ]
    """<p>The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point, that is used for all file operations by NFS clients using the access point. </p>"""
    root_directory: NotRequired[
        "capo_securityhub.types.aws_efs_access_point_root_directory_details.AwsEfsAccessPointRootDirectoryDetails"
    ]
    """<p>The directory on the Amazon EFS file system that the access point exposes as the root directory to NFS clients using the access point. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEfsAccessPointDetails) -> dict:
    out: dict = {}
    if "access_point_id" in value:
        out["AccessPointId"] = value["access_point_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "posix_user" in value:
        import capo_securityhub.types.aws_efs_access_point_posix_user_details

        out["PosixUser"] = (
            capo_securityhub.types.aws_efs_access_point_posix_user_details.serialize_json(
                value["posix_user"]
            )
        )
    if "root_directory" in value:
        import capo_securityhub.types.aws_efs_access_point_root_directory_details

        out["RootDirectory"] = (
            capo_securityhub.types.aws_efs_access_point_root_directory_details.serialize_json(
                value["root_directory"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEfsAccessPointDetails:
    out: AwsEfsAccessPointDetails = {}  # type: ignore[typeddict-item]
    if "AccessPointId" in data:
        out["access_point_id"] = data["AccessPointId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "PosixUser" in data:
        import capo_securityhub.types.aws_efs_access_point_posix_user_details

        out["posix_user"] = (
            capo_securityhub.types.aws_efs_access_point_posix_user_details.deserialize_json(
                data["PosixUser"]
            )
        )
    if "RootDirectory" in data:
        import capo_securityhub.types.aws_efs_access_point_root_directory_details

        out["root_directory"] = (
            capo_securityhub.types.aws_efs_access_point_root_directory_details.deserialize_json(
                data["RootDirectory"]
            )
        )
    return out
