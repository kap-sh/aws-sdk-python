"""Generated from Smithy shape ``com.amazonaws.fms#GetAdminAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.account_role_status
    import aws_sdk_fms.types.aws_account_id


class GetAdminAccountResponse(TypedDict):
    admin_account: NotRequired["aws_sdk_fms.types.aws_account_id.AWSAccountId"]
    """<p>The account that is set as the Firewall Manager default administrator.</p>"""
    role_status: NotRequired["aws_sdk_fms.types.account_role_status.AccountRoleStatus"]
    """<p>The status of the account that you set as the Firewall Manager default administrator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAdminAccountResponse) -> dict:
    out: dict = {}
    if "admin_account" in value:
        out["AdminAccount"] = value["admin_account"]
    if "role_status" in value:
        import aws_sdk_fms.types.account_role_status

        out["RoleStatus"] = (
            aws_sdk_fms.types.account_role_status.serialize_aws_json_1_1(
                value["role_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAdminAccountResponse:
    out: GetAdminAccountResponse = {}  # type: ignore[typeddict-item]
    if "AdminAccount" in data:
        out["admin_account"] = data["AdminAccount"]
    if "RoleStatus" in data:
        import aws_sdk_fms.types.account_role_status

        out["role_status"] = (
            aws_sdk_fms.types.account_role_status.deserialize_aws_json_1_1(
                data["RoleStatus"]
            )
        )
    return out
