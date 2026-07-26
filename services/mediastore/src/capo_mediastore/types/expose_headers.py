"""Generated from Smithy shape ``com.amazonaws.mediastore#ExposeHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediastore.types.header

ExposeHeaders: TypeAlias = list["capo_mediastore.types.header.Header"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExposeHeaders) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExposeHeaders:
    return list(data)
