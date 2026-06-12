"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateIPSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class CreateIPSetResponse(TypedDict):
    ip_set_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ID of the IPSet resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIPSetResponse) -> dict:
    out: dict = {}
    if "ip_set_id" in value:
        out["ipSetId"] = value["ip_set_id"]
    return out


def deserialize_json(data: dict) -> CreateIPSetResponse:
    out: CreateIPSetResponse = {}  # type: ignore[typeddict-item]
    if "ipSetId" in data:
        out["ip_set_id"] = data["ipSetId"]
    return out
