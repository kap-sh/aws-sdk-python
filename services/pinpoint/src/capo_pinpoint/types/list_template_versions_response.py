"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListTemplateVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.template_versions_response


class ListTemplateVersionsResponse(TypedDict, closed=True):
    template_versions_response: NotRequired[
        "capo_pinpoint.types.template_versions_response.TemplateVersionsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateVersionsResponse) -> dict:
    out: dict = {}
    if "template_versions_response" in value:
        import capo_pinpoint.types.template_versions_response

        out["TemplateVersionsResponse"] = (
            capo_pinpoint.types.template_versions_response.serialize_json(
                value["template_versions_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListTemplateVersionsResponse:
    out: ListTemplateVersionsResponse = {}  # type: ignore[typeddict-item]
    if "TemplateVersionsResponse" in data:
        import capo_pinpoint.types.template_versions_response

        out["template_versions_response"] = (
            capo_pinpoint.types.template_versions_response.deserialize_json(
                data["TemplateVersionsResponse"]
            )
        )
    return out
