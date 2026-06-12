"""Generated from Smithy shape ``com.amazonaws.connect#SuccessfulRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.request_identifier


class SuccessfulRequest(TypedDict):
    request_identifier: NotRequired[
        "aws_sdk_connect.types.request_identifier.RequestIdentifier"
    ]
    """<p>Request identifier provided in the API call in the ContactDataRequest to create a contact.</p>"""
    contact_id: NotRequired["aws_sdk_connect.types.contact_id.ContactId"]
    """<p>The contactId of the contact that was created successfully.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulRequest) -> dict:
    out: dict = {}
    if "request_identifier" in value:
        out["RequestIdentifier"] = value["request_identifier"]
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    return out


def deserialize_json(data: dict) -> SuccessfulRequest:
    out: SuccessfulRequest = {}  # type: ignore[typeddict-item]
    if "RequestIdentifier" in data:
        out["request_identifier"] = data["RequestIdentifier"]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    return out
