"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEfsAccessPointRootDirectoryDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_efs_access_point_root_directory_creation_info_details
    import capo_securityhub.types.non_empty_string


class AwsEfsAccessPointRootDirectoryDetails(TypedDict, closed=True):
    creation_info: NotRequired[
        "capo_securityhub.types.aws_efs_access_point_root_directory_creation_info_details.AwsEfsAccessPointRootDirectoryCreationInfoDetails"
    ]
    """<p>Specifies the POSIX IDs and permissions to apply to the access point's root directory. </p>"""
    path: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the path on the Amazon EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide <code>CreationInfo</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEfsAccessPointRootDirectoryDetails) -> dict:
    out: dict = {}
    if "creation_info" in value:
        import capo_securityhub.types.aws_efs_access_point_root_directory_creation_info_details

        out["CreationInfo"] = (
            capo_securityhub.types.aws_efs_access_point_root_directory_creation_info_details.serialize_json(
                value["creation_info"]
            )
        )
    if "path" in value:
        out["Path"] = value["path"]
    return out


def deserialize_json(data: dict) -> AwsEfsAccessPointRootDirectoryDetails:
    out: AwsEfsAccessPointRootDirectoryDetails = {}  # type: ignore[typeddict-item]
    if "CreationInfo" in data:
        import capo_securityhub.types.aws_efs_access_point_root_directory_creation_info_details

        out["creation_info"] = (
            capo_securityhub.types.aws_efs_access_point_root_directory_creation_info_details.deserialize_json(
                data["CreationInfo"]
            )
        )
    if "Path" in data:
        out["path"] = data["Path"]
    return out
