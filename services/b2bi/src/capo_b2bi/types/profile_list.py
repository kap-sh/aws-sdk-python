"""Generated from Smithy shape ``com.amazonaws.b2bi#ProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_b2bi.types.profile_summary

ProfileList: TypeAlias = list["capo_b2bi.types.profile_summary.ProfileSummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProfileList) -> list:
    import capo_b2bi.types.profile_summary

    out: list = []
    for item in value:
        out.append(capo_b2bi.types.profile_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ProfileList:
    import capo_b2bi.types.profile_summary

    out: ProfileList = []
    for item in data:
        out.append(capo_b2bi.types.profile_summary.deserialize_aws_json_1_0(item))
    return out
