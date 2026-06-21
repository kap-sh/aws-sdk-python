"""Generated from Smithy shape ``com.amazonaws.sagemaker#UserProfileSortKey``."""

from typing import Literal, TypeAlias, cast

UserProfileSortKey: TypeAlias = Literal[
    "CreationTime",
    "LastModifiedTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserProfileSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserProfileSortKey:
    return cast(UserProfileSortKey, data)
