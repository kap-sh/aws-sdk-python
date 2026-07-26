"""Generated from Smithy shape ``com.amazonaws.emr#OSReleaseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.os_release

OSReleaseList: TypeAlias = list["capo_emr.types.os_release.OSRelease"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OSReleaseList) -> list:
    import capo_emr.types.os_release

    out: list = []
    for item in value:
        out.append(capo_emr.types.os_release.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OSReleaseList:
    import capo_emr.types.os_release

    out: OSReleaseList = []
    for item in data:
        out.append(capo_emr.types.os_release.deserialize_aws_json_1_1(item))
    return out
