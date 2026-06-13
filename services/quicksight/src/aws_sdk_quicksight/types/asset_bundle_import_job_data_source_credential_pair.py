"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSourceCredentialPair``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.db_username
    import aws_sdk_quicksight.types.password


class AssetBundleImportJobDataSourceCredentialPair(TypedDict):
    username: "aws_sdk_quicksight.types.db_username.DbUsername"
    """<p>The username for the data source connection.</p>"""
    password: "aws_sdk_quicksight.types.password.Password"
    """<p>The password for the data source connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSourceCredentialPair) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    out["Password"] = value["password"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDataSourceCredentialPair:
    out: AssetBundleImportJobDataSourceCredentialPair = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError(
            "AssetBundleImportJobDataSourceCredentialPair.username required"
        )
    if "Password" in data:
        out["password"] = data["Password"]
    else:
        raise DeserializationError(
            "AssetBundleImportJobDataSourceCredentialPair.password required"
        )
    return out
