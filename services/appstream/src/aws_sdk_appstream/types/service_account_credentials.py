"""Generated from Smithy shape ``com.amazonaws.appstream#ServiceAccountCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.account_name
    import aws_sdk_appstream.types.account_password


class ServiceAccountCredentials(TypedDict, closed=True):
    account_name: NotRequired["aws_sdk_appstream.types.account_name.AccountName"]
    """<p>The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.</p>"""
    account_password: NotRequired[
        "aws_sdk_appstream.types.account_password.AccountPassword"
    ]
    """<p>The password for the account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceAccountCredentials) -> dict:
    out: dict = {}
    if "account_name" in value:
        out["AccountName"] = value["account_name"]
    if "account_password" in value:
        out["AccountPassword"] = value["account_password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceAccountCredentials:
    out: ServiceAccountCredentials = {}  # type: ignore[typeddict-item]
    if "AccountName" in data:
        out["account_name"] = data["AccountName"]
    if "AccountPassword" in data:
        out["account_password"] = data["AccountPassword"]
    return out
