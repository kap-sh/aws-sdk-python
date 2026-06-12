"""Generated from Smithy shape ``com.amazonaws.sso#RoleInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso.types.account_id_type
    import aws_sdk_sso.types.role_name_type


class RoleInfo(TypedDict):
    role_name: NotRequired["aws_sdk_sso.types.role_name_type.RoleNameType"]
    """<p>The friendly name of the role that is assigned to the user.</p>"""
    account_id: NotRequired["aws_sdk_sso.types.account_id_type.AccountIdType"]
    """<p>The identifier of the AWS account assigned to the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoleInfo) -> dict:
    out: dict = {}
    if "role_name" in value:
        out["roleName"] = value["role_name"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> RoleInfo:
    out: RoleInfo = {}  # type: ignore[typeddict-item]
    if "roleName" in data:
        out["role_name"] = data["roleName"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    return out
