"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#GroupSharingPreferenceEnum``."""

from typing import Literal, TypeAlias, cast

GroupSharingPreferenceEnum: TypeAlias = Literal[
    "OPEN",
    "PRIORITIZED",
    "RESTRICTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GroupSharingPreferenceEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GroupSharingPreferenceEnum:
    return cast(GroupSharingPreferenceEnum, data)
