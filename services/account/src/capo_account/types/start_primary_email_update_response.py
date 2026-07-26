"""Generated from Smithy shape ``com.amazonaws.account#StartPrimaryEmailUpdateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account.types.primary_email_update_status


class StartPrimaryEmailUpdateResponse(TypedDict, closed=True):
    status: NotRequired[
        "capo_account.types.primary_email_update_status.PrimaryEmailUpdateStatus"
    ]
    """<p>The status of the primary email update request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPrimaryEmailUpdateResponse) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> StartPrimaryEmailUpdateResponse:
    out: StartPrimaryEmailUpdateResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
