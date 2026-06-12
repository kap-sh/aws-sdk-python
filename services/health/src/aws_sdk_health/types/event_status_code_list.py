"""Generated from Smithy shape ``com.amazonaws.health#eventStatusCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.event_status_code

eventStatusCodeList: TypeAlias = list[
    "aws_sdk_health.types.event_status_code.eventStatusCode"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: eventStatusCodeList) -> list:
    import aws_sdk_health.types.event_status_code

    out: list = []
    for item in value:
        out.append(aws_sdk_health.types.event_status_code.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> eventStatusCodeList:
    import aws_sdk_health.types.event_status_code

    out: eventStatusCodeList = []
    for item in data:
        out.append(
            aws_sdk_health.types.event_status_code.deserialize_aws_json_1_1(item)
        )
    return out
