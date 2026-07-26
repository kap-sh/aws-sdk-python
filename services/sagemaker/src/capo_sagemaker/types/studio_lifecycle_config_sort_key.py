"""Generated from Smithy shape ``com.amazonaws.sagemaker#StudioLifecycleConfigSortKey``."""

from typing import Literal, TypeAlias, cast

StudioLifecycleConfigSortKey: TypeAlias = Literal[
    "CreationTime",
    "LastModifiedTime",
    "Name",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StudioLifecycleConfigSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StudioLifecycleConfigSortKey:
    return cast(StudioLifecycleConfigSortKey, data)
