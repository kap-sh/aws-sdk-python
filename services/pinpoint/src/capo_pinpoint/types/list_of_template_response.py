"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfTemplateResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.template_response

ListOfTemplateResponse: TypeAlias = list[
    "capo_pinpoint.types.template_response.TemplateResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfTemplateResponse) -> list:
    import capo_pinpoint.types.template_response

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.template_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfTemplateResponse:
    import capo_pinpoint.types.template_response

    out: ListOfTemplateResponse = []
    for item in data:
        out.append(capo_pinpoint.types.template_response.deserialize_json(item))
    return out
