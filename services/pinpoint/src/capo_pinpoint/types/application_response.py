"""Generated from Smithy shape ``com.amazonaws.pinpoint#ApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.map_of__string


class ApplicationResponse(TypedDict, closed=True):
    arn: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The display name of the application. This name is displayed as the <b>Project name</b> on the Amazon Pinpoint console.</p>"""
    tags: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A string-to-string map of key-value pairs that identifies the tags that are associated with the application. Each tag consists of a required tag key and an associated tag value.</p>"""
    creation_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time when the Application was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "tags" in value:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.serialize_json(value["tags"])
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    return out


def deserialize_json(data: dict) -> ApplicationResponse:
    out: ApplicationResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "tags" in data:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.deserialize_json(data["tags"])
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    return out
