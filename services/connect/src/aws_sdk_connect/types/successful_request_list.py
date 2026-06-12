"""Generated from Smithy shape ``com.amazonaws.connect#SuccessfulRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.successful_request

SuccessfulRequestList: TypeAlias = list[
    "aws_sdk_connect.types.successful_request.SuccessfulRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulRequestList) -> list:
    import aws_sdk_connect.types.successful_request

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.successful_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> SuccessfulRequestList:
    import aws_sdk_connect.types.successful_request

    out: SuccessfulRequestList = []
    for item in data:
        out.append(aws_sdk_connect.types.successful_request.deserialize_json(item))
    return out
