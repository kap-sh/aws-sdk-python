"""Generated from Smithy shape ``com.amazonaws.quicksight#SignupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.string


class SignupResponse(TypedDict, closed=True):
    iam_user: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean that is <code>TRUE</code> if the Amazon Quick Sight uses IAM as an authentication method.</p>"""
    user_login_name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The user login name for your Amazon Quick Sight account.</p>"""
    account_name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The name of your Quick Sight account.</p>"""
    directory_type: NotRequired["capo_quicksight.types.string.String"]
    """<p>The type of Active Directory that is being used to authenticate the Amazon Quick Sight account. Valid values are <code>SIMPLE_AD</code>, <code>AD_CONNECTOR</code>, and <code>MICROSOFT_AD</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SignupResponse) -> dict:
    out: dict = {}
    out["IAMUser"] = value.get("iam_user", False)
    if "user_login_name" in value:
        out["userLoginName"] = value["user_login_name"]
    if "account_name" in value:
        out["accountName"] = value["account_name"]
    if "directory_type" in value:
        out["directoryType"] = value["directory_type"]
    return out


def deserialize_json(data: dict) -> SignupResponse:
    out: SignupResponse = {}  # type: ignore[typeddict-item]
    if "IAMUser" in data:
        out["iam_user"] = data["IAMUser"]
    else:
        out["iam_user"] = False
    if "userLoginName" in data:
        out["user_login_name"] = data["userLoginName"]
    if "accountName" in data:
        out["account_name"] = data["accountName"]
    if "directoryType" in data:
        out["directory_type"] = data["directoryType"]
    return out
