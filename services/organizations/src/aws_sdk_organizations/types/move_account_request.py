"""Generated from Smithy shape ``com.amazonaws.organizations#MoveAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.account_id
    import aws_sdk_organizations.types.parent_id


class MoveAccountRequest(TypedDict):
    account_id: "aws_sdk_organizations.types.account_id.AccountId"
    r"""<p>ID for the account that you want to move.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> for an account ID string requires exactly 12 digits.</p>"""
    source_parent_id: "aws_sdk_organizations.types.parent_id.ParentId"
    r"""<p>ID for the root or organizational unit that you want to move the account from.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> for a parent ID string requires one of the following:</p> <ul> <li> <p> <b>Root</b> - A string that begins with \"r-\" followed by from 4 to 32 lowercase letters or digits.</p> </li> <li> <p> <b>Organizational unit (OU)</b> - A string that begins with \"ou-\" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second \"-\" dash and from 8 to 32 additional lowercase letters or digits.</p> </li> </ul>"""
    destination_parent_id: "aws_sdk_organizations.types.parent_id.ParentId"
    r"""<p>ID for the root or organizational unit that you want to move the account to.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> for a parent ID string requires one of the following:</p> <ul> <li> <p> <b>Root</b> - A string that begins with \"r-\" followed by from 4 to 32 lowercase letters or digits.</p> </li> <li> <p> <b>Organizational unit (OU)</b> - A string that begins with \"ou-\" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second \"-\" dash and from 8 to 32 additional lowercase letters or digits.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MoveAccountRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["SourceParentId"] = value["source_parent_id"]
    out["DestinationParentId"] = value["destination_parent_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MoveAccountRequest:
    out: MoveAccountRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("MoveAccountRequest.account_id required")
    if "SourceParentId" in data:
        out["source_parent_id"] = data["SourceParentId"]
    else:
        raise DeserializationError("MoveAccountRequest.source_parent_id required")
    if "DestinationParentId" in data:
        out["destination_parent_id"] = data["DestinationParentId"]
    else:
        raise DeserializationError("MoveAccountRequest.destination_parent_id required")
    return out
