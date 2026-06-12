"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListTemplatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class ListTemplatesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>"""
    page_size: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>"""
    prefix: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The substring to match in the names of the message templates to include in the results. If you specify this value, Amazon Pinpoint returns only those templates whose names begin with the value that you specify.</p>"""
    template_type: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The type of message template to include in the results. Valid values are: EMAIL, PUSH, SMS, and VOICE. To include all types of templates in the results, don't include this parameter in your request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTemplatesRequest:
    out: ListTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
