"""Generated from Smithy shape ``com.amazonaws.opensearch#MasterUserOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.arn
    import capo_opensearch.types.password
    import capo_opensearch.types.username


class MasterUserOptions(TypedDict, closed=True):
    master_user_arn: NotRequired["capo_opensearch.types.arn.ARN"]
    """<p>Amazon Resource Name (ARN) for the master user. Only specify if <code>InternalUserDatabaseEnabled</code> is <code>false</code>.</p>"""
    master_user_name: NotRequired["capo_opensearch.types.username.Username"]
    """<p>User name for the master user. Only specify if <code>InternalUserDatabaseEnabled</code> is <code>true</code>.</p>"""
    master_user_password: NotRequired["capo_opensearch.types.password.Password"]
    """<p>Password for the master user. Only specify if <code>InternalUserDatabaseEnabled</code> is <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MasterUserOptions) -> dict:
    out: dict = {}
    if "master_user_arn" in value:
        out["MasterUserARN"] = value["master_user_arn"]
    if "master_user_name" in value:
        out["MasterUserName"] = value["master_user_name"]
    if "master_user_password" in value:
        out["MasterUserPassword"] = value["master_user_password"]
    return out


def deserialize_json(data: dict) -> MasterUserOptions:
    out: MasterUserOptions = {}  # type: ignore[typeddict-item]
    if "MasterUserARN" in data:
        out["master_user_arn"] = data["MasterUserARN"]
    if "MasterUserName" in data:
        out["master_user_name"] = data["MasterUserName"]
    if "MasterUserPassword" in data:
        out["master_user_password"] = data["MasterUserPassword"]
    return out
