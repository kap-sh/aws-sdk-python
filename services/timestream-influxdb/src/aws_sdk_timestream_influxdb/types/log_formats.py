"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#LogFormats``."""

from typing import Literal, TypeAlias, cast

LogFormats: TypeAlias = Literal["full",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LogFormats) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LogFormats:
    return cast(LogFormats, data)
