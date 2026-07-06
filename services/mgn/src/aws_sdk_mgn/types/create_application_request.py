"""Generated from Smithy shape ``com.amazonaws.mgn#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.application_description
    import aws_sdk_mgn.types.application_name
    import aws_sdk_mgn.types.tags_map


class CreateApplicationRequest(TypedDict, closed=True):
    name: "aws_sdk_mgn.types.application_name.ApplicationName"
    """<p>Application name.</p>"""
    description: NotRequired[
        "aws_sdk_mgn.types.application_description.ApplicationDescription"
    ]
    """<p>Application description.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Application tags.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
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
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
