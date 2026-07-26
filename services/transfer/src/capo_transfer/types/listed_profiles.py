"""Generated from Smithy shape ``com.amazonaws.transfer#ListedProfiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.listed_profile

ListedProfiles: TypeAlias = list["capo_transfer.types.listed_profile.ListedProfile"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedProfiles) -> list:
    import capo_transfer.types.listed_profile

    out: list = []
    for item in value:
        out.append(capo_transfer.types.listed_profile.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListedProfiles:
    import capo_transfer.types.listed_profile

    out: ListedProfiles = []
    for item in data:
        out.append(capo_transfer.types.listed_profile.deserialize_aws_json_1_1(item))
    return out
