"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppImageConfigSortKey``."""

from typing import Literal, TypeAlias, cast

AppImageConfigSortKey: TypeAlias = Literal[
    "CreationTime",
    "LastModifiedTime",
    "Name",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppImageConfigSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppImageConfigSortKey:
    return cast(AppImageConfigSortKey, data)
