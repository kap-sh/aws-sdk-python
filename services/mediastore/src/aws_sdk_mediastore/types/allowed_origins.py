"""Generated from Smithy shape ``com.amazonaws.mediastore#AllowedOrigins``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.origin

AllowedOrigins: TypeAlias = list["aws_sdk_mediastore.types.origin.Origin"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedOrigins) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AllowedOrigins:
    return list(data)
