"""Generated from Smithy shape ``com.amazonaws.account#AcceptPrimaryEmailUpdateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_account.types.primary_email_update_status


class AcceptPrimaryEmailUpdateResponse(TypedDict):
    status: NotRequired[
        "aws_sdk_account.types.primary_email_update_status.PrimaryEmailUpdateStatus"
    ]
    """<p>Retrieves the status of the accepted primary email update request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptPrimaryEmailUpdateResponse) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AcceptPrimaryEmailUpdateResponse:
    out: AcceptPrimaryEmailUpdateResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
