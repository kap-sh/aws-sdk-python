"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfTemplateVersionResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.template_version_response

ListOfTemplateVersionResponse: TypeAlias = list[
    "capo_pinpoint.types.template_version_response.TemplateVersionResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfTemplateVersionResponse) -> list:
    import capo_pinpoint.types.template_version_response

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.template_version_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfTemplateVersionResponse:
    import capo_pinpoint.types.template_version_response

    out: ListOfTemplateVersionResponse = []
    for item in data:
        out.append(capo_pinpoint.types.template_version_response.deserialize_json(item))
    return out
