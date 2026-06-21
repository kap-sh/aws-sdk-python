"""Generated from Smithy shape ``com.amazonaws.dynamodb#StreamViewType``."""

from typing import Literal, TypeAlias, cast

StreamViewType: TypeAlias = Literal[
    "NEW_IMAGE",
    "OLD_IMAGE",
    "NEW_AND_OLD_IMAGES",
    "KEYS_ONLY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StreamViewType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StreamViewType:
    return cast(StreamViewType, data)
