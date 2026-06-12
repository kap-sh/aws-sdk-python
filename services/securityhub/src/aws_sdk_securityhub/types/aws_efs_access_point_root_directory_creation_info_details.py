"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEfsAccessPointRootDirectoryCreationInfoDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEfsAccessPointRootDirectoryCreationInfoDetails(TypedDict):
    owner_gid: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the POSIX group ID to apply to the root directory. </p>"""
    owner_uid: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the POSIX user ID to apply to the root directory. </p>"""
    permissions: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Specifies the POSIX permissions to apply to the root directory, in the format of an octal number representing the file's mode bits. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEfsAccessPointRootDirectoryCreationInfoDetails) -> dict:
    out: dict = {}
    if "owner_gid" in value:
        out["OwnerGid"] = value["owner_gid"]
    if "owner_uid" in value:
        out["OwnerUid"] = value["owner_uid"]
    if "permissions" in value:
        out["Permissions"] = value["permissions"]
    return out


def deserialize_json(data: dict) -> AwsEfsAccessPointRootDirectoryCreationInfoDetails:
    out: AwsEfsAccessPointRootDirectoryCreationInfoDetails = {}  # type: ignore[typeddict-item]
    if "OwnerGid" in data:
        out["owner_gid"] = data["OwnerGid"]
    if "OwnerUid" in data:
        out["owner_uid"] = data["OwnerUid"]
    if "Permissions" in data:
        out["permissions"] = data["Permissions"]
    return out
