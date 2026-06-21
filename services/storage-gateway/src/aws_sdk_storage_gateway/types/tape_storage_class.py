"""Generated from Smithy shape ``com.amazonaws.storagegateway#TapeStorageClass``."""

from typing import Literal, TypeAlias, cast

TapeStorageClass: TypeAlias = Literal[
    "DEEP_ARCHIVE",
    "GLACIER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TapeStorageClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TapeStorageClass:
    return cast(TapeStorageClass, data)
