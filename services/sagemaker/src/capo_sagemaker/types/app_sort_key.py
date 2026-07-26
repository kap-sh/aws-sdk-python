"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppSortKey``."""

from typing import Literal, TypeAlias, cast

AppSortKey: TypeAlias = Literal["CreationTime",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppSortKey:
    return cast(AppSortKey, data)
