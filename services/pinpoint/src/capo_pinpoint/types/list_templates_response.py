"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.templates_response


class ListTemplatesResponse(TypedDict, closed=True):
    templates_response: NotRequired[
        "capo_pinpoint.types.templates_response.TemplatesResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplatesResponse) -> dict:
    out: dict = {}
    if "templates_response" in value:
        import capo_pinpoint.types.templates_response

        out["TemplatesResponse"] = (
            capo_pinpoint.types.templates_response.serialize_json(
                value["templates_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListTemplatesResponse:
    out: ListTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "TemplatesResponse" in data:
        import capo_pinpoint.types.templates_response

        out["templates_response"] = (
            capo_pinpoint.types.templates_response.deserialize_json(
                data["TemplatesResponse"]
            )
        )
    return out
