"""Generated from Smithy shape ``com.amazonaws.iot#HeaderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.http_action_header

HeaderList: TypeAlias = list["aws_sdk_iot.types.http_action_header.HttpActionHeader"]


# --- restJson1 ser/de ---
def serialize_json(value: HeaderList) -> list:
    import aws_sdk_iot.types.http_action_header

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.http_action_header.serialize_json(item))
    return out


def deserialize_json(data: list) -> HeaderList:
    import aws_sdk_iot.types.http_action_header

    out: HeaderList = []
    for item in data:
        out.append(aws_sdk_iot.types.http_action_header.deserialize_json(item))
    return out
