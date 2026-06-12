"""Generated from Smithy shape ``com.amazonaws.iotwireless#ServiceProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.service_profile

ServiceProfileList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.service_profile.ServiceProfile"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceProfileList) -> list:
    import aws_sdk_iot_wireless.types.service_profile

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_wireless.types.service_profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceProfileList:
    import aws_sdk_iot_wireless.types.service_profile

    out: ServiceProfileList = []
    for item in data:
        out.append(aws_sdk_iot_wireless.types.service_profile.deserialize_json(item))
    return out
