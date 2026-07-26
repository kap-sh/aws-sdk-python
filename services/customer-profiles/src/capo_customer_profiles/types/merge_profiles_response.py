"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MergeProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.message


class MergeProfilesResponse(TypedDict, closed=True):
    message: NotRequired["capo_customer_profiles.types.message.message"]
    """<p>A message that indicates the merge request is complete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MergeProfilesResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MergeProfilesResponse:
    out: MergeProfilesResponse = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
