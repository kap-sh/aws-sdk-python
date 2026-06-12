"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DedicatedIpList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.dedicated_ip

DedicatedIpList: TypeAlias = list[
    "aws_sdk_pinpoint_email.types.dedicated_ip.DedicatedIp"
]


# --- restJson1 ser/de ---
def serialize_json(value: DedicatedIpList) -> list:
    import aws_sdk_pinpoint_email.types.dedicated_ip

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint_email.types.dedicated_ip.serialize_json(item))
    return out


def deserialize_json(data: list) -> DedicatedIpList:
    import aws_sdk_pinpoint_email.types.dedicated_ip

    out: DedicatedIpList = []
    for item in data:
        out.append(aws_sdk_pinpoint_email.types.dedicated_ip.deserialize_json(item))
    return out
