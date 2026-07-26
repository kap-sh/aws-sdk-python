"""Generated from Smithy shape ``com.amazonaws.mgn#UnarchiveApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.application_id


class UnarchiveApplicationRequest(TypedDict, closed=True):
    application_id: "capo_mgn.types.application_id.ApplicationID"
    """<p>Application ID.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnarchiveApplicationRequest) -> dict:
    out: dict = {}
    out["applicationID"] = value["application_id"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> UnarchiveApplicationRequest:
    out: UnarchiveApplicationRequest = {}  # type: ignore[typeddict-item]
    if "applicationID" in data:
        out["application_id"] = data["applicationID"]
    else:
        raise DeserializationError(
            "UnarchiveApplicationRequest.application_id required"
        )
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
