"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfApplicationResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.application_response

ListOfApplicationResponse: TypeAlias = list[
    "aws_sdk_pinpoint.types.application_response.ApplicationResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfApplicationResponse) -> list:
    import aws_sdk_pinpoint.types.application_response

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.application_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfApplicationResponse:
    import aws_sdk_pinpoint.types.application_response

    out: ListOfApplicationResponse = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.application_response.deserialize_json(item))
    return out
