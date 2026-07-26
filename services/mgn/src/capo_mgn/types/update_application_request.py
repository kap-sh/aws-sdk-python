"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.application_description
    import capo_mgn.types.application_id
    import capo_mgn.types.application_name


class UpdateApplicationRequest(TypedDict, closed=True):
    application_id: "capo_mgn.types.application_id.ApplicationID"
    """<p>Application ID.</p>"""
    name: NotRequired["capo_mgn.types.application_name.ApplicationName"]
    """<p>Application name.</p>"""
    description: NotRequired[
        "capo_mgn.types.application_description.ApplicationDescription"
    ]
    """<p>Application description.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    out["applicationID"] = value["application_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "applicationID" in data:
        out["application_id"] = data["applicationID"]
    else:
        raise DeserializationError("UpdateApplicationRequest.application_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
