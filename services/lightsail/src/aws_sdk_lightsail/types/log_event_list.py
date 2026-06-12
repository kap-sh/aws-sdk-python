"""Generated from Smithy shape ``com.amazonaws.lightsail#LogEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.log_event

LogEventList: TypeAlias = list["aws_sdk_lightsail.types.log_event.LogEvent"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogEventList) -> list:
    import aws_sdk_lightsail.types.log_event

    out: list = []
    for item in value:
        out.append(aws_sdk_lightsail.types.log_event.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LogEventList:
    import aws_sdk_lightsail.types.log_event

    out: LogEventList = []
    for item in data:
        out.append(aws_sdk_lightsail.types.log_event.deserialize_aws_json_1_1(item))
    return out
