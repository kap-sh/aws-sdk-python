"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfActivityResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.activity_response

ListOfActivityResponse: TypeAlias = list[
    "aws_sdk_pinpoint.types.activity_response.ActivityResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfActivityResponse) -> list:
    import aws_sdk_pinpoint.types.activity_response

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.activity_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfActivityResponse:
    import aws_sdk_pinpoint.types.activity_response

    out: ListOfActivityResponse = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.activity_response.deserialize_json(item))
    return out
