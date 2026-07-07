"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteSegmentDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.string1_to1000


class DeleteSegmentDefinitionResponse(TypedDict, closed=True):
    message: NotRequired["aws_sdk_customer_profiles.types.string1_to1000.string1To1000"]
    """<p>A message that indicates the delete request is done.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSegmentDefinitionResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteSegmentDefinitionResponse:
    out: DeleteSegmentDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
