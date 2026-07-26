"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEfsAccessPointPosixUserDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsEfsAccessPointPosixUserDetails(TypedDict, closed=True):
    gid: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The POSIX group ID used for all file system operations using this access point. </p>"""
    secondary_gids: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>Secondary POSIX group IDs used for all file system operations using this access point. </p>"""
    uid: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The POSIX user ID used for all file system operations using this access point. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEfsAccessPointPosixUserDetails) -> dict:
    out: dict = {}
    if "gid" in value:
        out["Gid"] = value["gid"]
    if "secondary_gids" in value:
        import capo_securityhub.types.non_empty_string_list

        out["SecondaryGids"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["secondary_gids"]
            )
        )
    if "uid" in value:
        out["Uid"] = value["uid"]
    return out


def deserialize_json(data: dict) -> AwsEfsAccessPointPosixUserDetails:
    out: AwsEfsAccessPointPosixUserDetails = {}  # type: ignore[typeddict-item]
    if "Gid" in data:
        out["gid"] = data["Gid"]
    if "SecondaryGids" in data:
        import capo_securityhub.types.non_empty_string_list

        out["secondary_gids"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["SecondaryGids"]
            )
        )
    if "Uid" in data:
        out["uid"] = data["Uid"]
    return out
