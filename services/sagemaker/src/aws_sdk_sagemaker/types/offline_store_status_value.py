"""Generated from Smithy shape ``com.amazonaws.sagemaker#OfflineStoreStatusValue``."""

from typing import Literal, TypeAlias, cast

OfflineStoreStatusValue: TypeAlias = Literal[
    "Active",
    "Blocked",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OfflineStoreStatusValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OfflineStoreStatusValue:
    return cast(OfflineStoreStatusValue, data)
