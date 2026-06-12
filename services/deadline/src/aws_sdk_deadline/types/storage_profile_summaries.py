"""Generated from Smithy shape ``com.amazonaws.deadline#StorageProfileSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.storage_profile_summary

StorageProfileSummaries: TypeAlias = list[
    "aws_sdk_deadline.types.storage_profile_summary.StorageProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageProfileSummaries) -> list:
    import aws_sdk_deadline.types.storage_profile_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.storage_profile_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> StorageProfileSummaries:
    import aws_sdk_deadline.types.storage_profile_summary

    out: StorageProfileSummaries = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.storage_profile_summary.deserialize_json(item)
        )
    return out
