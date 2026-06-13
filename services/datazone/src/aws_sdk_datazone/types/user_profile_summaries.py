"""Generated from Smithy shape ``com.amazonaws.datazone#UserProfileSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.user_profile_summary

UserProfileSummaries: TypeAlias = list[
    "aws_sdk_datazone.types.user_profile_summary.UserProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserProfileSummaries) -> list:
    import aws_sdk_datazone.types.user_profile_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.user_profile_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserProfileSummaries:
    import aws_sdk_datazone.types.user_profile_summary

    out: UserProfileSummaries = []
    for item in data:
        out.append(aws_sdk_datazone.types.user_profile_summary.deserialize_json(item))
    return out
