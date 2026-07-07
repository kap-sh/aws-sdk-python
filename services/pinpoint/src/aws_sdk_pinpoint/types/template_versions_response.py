"""Generated from Smithy shape ``com.amazonaws.pinpoint#TemplateVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.list_of_template_version_response


class TemplateVersionsResponse(TypedDict, closed=True):
    item: NotRequired[
        "aws_sdk_pinpoint.types.list_of_template_version_response.ListOfTemplateVersionResponse"
    ]
    """<p>An array of responses, one for each version of the message template.</p>"""
    message: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The message that's returned from the API for the request to retrieve information about all the versions of the message template.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""
    request_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the request to retrieve information about all the versions of the message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateVersionsResponse) -> dict:
    out: dict = {}
    if "item" in value:
        import aws_sdk_pinpoint.types.list_of_template_version_response

        out["Item"] = (
            aws_sdk_pinpoint.types.list_of_template_version_response.serialize_json(
                value["item"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestID"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> TemplateVersionsResponse:
    out: TemplateVersionsResponse = {}  # type: ignore[typeddict-item]
    if "Item" in data:
        import aws_sdk_pinpoint.types.list_of_template_version_response

        out["item"] = (
            aws_sdk_pinpoint.types.list_of_template_version_response.deserialize_json(
                data["Item"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestID" in data:
        out["request_id"] = data["RequestID"]
    return out
