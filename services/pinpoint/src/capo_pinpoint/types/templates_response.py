"""Generated from Smithy shape ``com.amazonaws.pinpoint#TemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.list_of_template_response


class TemplatesResponse(TypedDict, closed=True):
    item: NotRequired[
        "capo_pinpoint.types.list_of_template_response.ListOfTemplateResponse"
    ]
    """<p>An array of responses, one for each message template that's associated with your Amazon Pinpoint account and meets any filter criteria that you specified in the request.</p>"""
    next_token: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplatesResponse) -> dict:
    out: dict = {}
    if "item" in value:
        import capo_pinpoint.types.list_of_template_response

        out["Item"] = capo_pinpoint.types.list_of_template_response.serialize_json(
            value["item"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> TemplatesResponse:
    out: TemplatesResponse = {}  # type: ignore[typeddict-item]
    if "Item" in data:
        import capo_pinpoint.types.list_of_template_response

        out["item"] = capo_pinpoint.types.list_of_template_response.deserialize_json(
            data["Item"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
