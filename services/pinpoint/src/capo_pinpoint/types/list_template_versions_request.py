"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListTemplateVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string


class ListTemplateVersionsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>"""
    page_size: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>"""
    template_name: "capo_pinpoint.types.__string.__string"
    """<p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>"""
    template_type: "capo_pinpoint.types.__string.__string"
    """<p>The type of channel that the message template is designed for. Valid values are: EMAIL, PUSH, SMS, and VOICE.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTemplateVersionsRequest:
    out: ListTemplateVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
