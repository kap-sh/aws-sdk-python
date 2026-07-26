"""Generated from Smithy shape ``com.amazonaws.mgn#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.application_description
    import capo_mgn.types.application_name
    import capo_mgn.types.tags_map


class CreateApplicationRequest(TypedDict, closed=True):
    name: "capo_mgn.types.application_name.ApplicationName"
    """<p>Application name.</p>"""
    description: NotRequired[
        "capo_mgn.types.application_description.ApplicationDescription"
    ]
    """<p>Application description.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Application tags.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateApplicationRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
