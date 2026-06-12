"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfTemplateResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.template_response

ListOfTemplateResponse: TypeAlias = list[
    "aws_sdk_pinpoint.types.template_response.TemplateResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfTemplateResponse) -> list:
    import aws_sdk_pinpoint.types.template_response

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.template_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfTemplateResponse:
    import aws_sdk_pinpoint.types.template_response

    out: ListOfTemplateResponse = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.template_response.deserialize_json(item))
    return out
