"""Generated from Smithy shape ``com.amazonaws.mediastore#AllowedHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediastore.types.header

AllowedHeaders: TypeAlias = list["capo_mediastore.types.header.Header"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedHeaders) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AllowedHeaders:
    return list(data)
