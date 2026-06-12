"""Generated from Smithy shape ``com.amazonaws.codecatalyst#UserIdentity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.user_type


class UserIdentity(TypedDict):
    user_type: "aws_sdk_codecatalyst.types.user_type.UserType"
    """<p>The role assigned to the user in a Amazon CodeCatalyst space or project when the event occurred.</p>"""
    principal_id: "str"
    """<p>The ID of the Amazon CodeCatalyst service principal.</p>"""
    user_name: NotRequired["str"]
    """<p>The display name of the user in Amazon CodeCatalyst.</p>"""
    aws_account_id: NotRequired["str"]
    """<p>The Amazon Web Services account number of the user in Amazon Web Services, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserIdentity) -> dict:
    out: dict = {}
    out["userType"] = value["user_type"]
    out["principalId"] = value["principal_id"]
    if "user_name" in value:
        out["userName"] = value["user_name"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    return out


def deserialize_json(data: dict) -> UserIdentity:
    out: UserIdentity = {}  # type: ignore[typeddict-item]
    if "userType" in data:
        out["user_type"] = data["userType"]
    else:
        raise DeserializationError("UserIdentity.user_type required")
    if "principalId" in data:
        out["principal_id"] = data["principalId"]
    else:
        raise DeserializationError("UserIdentity.principal_id required")
    if "userName" in data:
        out["user_name"] = data["userName"]
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    return out
