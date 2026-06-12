"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListTemplateVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.template_versions_response


class ListTemplateVersionsResponse(TypedDict):
    template_versions_response: NotRequired[
        "aws_sdk_pinpoint.types.template_versions_response.TemplateVersionsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateVersionsResponse) -> dict:
    out: dict = {}
    if "template_versions_response" in value:
        import aws_sdk_pinpoint.types.template_versions_response

        out["TemplateVersionsResponse"] = (
            aws_sdk_pinpoint.types.template_versions_response.serialize_json(
                value["template_versions_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListTemplateVersionsResponse:
    out: ListTemplateVersionsResponse = {}  # type: ignore[typeddict-item]
    if "TemplateVersionsResponse" in data:
        import aws_sdk_pinpoint.types.template_versions_response

        out["template_versions_response"] = (
            aws_sdk_pinpoint.types.template_versions_response.deserialize_json(
                data["TemplateVersionsResponse"]
            )
        )
    return out
