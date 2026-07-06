"""Generated from Smithy shape ``com.amazonaws.fms#PutAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.admin_scope
    import aws_sdk_fms.types.aws_account_id


class PutAdminAccountRequest(TypedDict, closed=True):
    admin_account: "aws_sdk_fms.types.aws_account_id.AWSAccountId"
    r"""<p>The Amazon Web Services account ID to add as an Firewall Manager administrator account. The account must be a member of the organization that was onboarded to Firewall Manager by <a>AssociateAdminAccount</a>. For more information about Organizations, see <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html\">Managing the Amazon Web Services Accounts in Your Organization</a>.</p>"""
    admin_scope: NotRequired["aws_sdk_fms.types.admin_scope.AdminScope"]
    """<p>Configures the resources that the specified Firewall Manager administrator can manage. As a best practice, set the administrative scope according to the principles of least privilege. Only grant the administrator the specific resources or permissions that they need to perform the duties of their role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAdminAccountRequest) -> dict:
    out: dict = {}
    out["AdminAccount"] = value["admin_account"]
    if "admin_scope" in value:
        import aws_sdk_fms.types.admin_scope

        out["AdminScope"] = aws_sdk_fms.types.admin_scope.serialize_aws_json_1_1(
            value["admin_scope"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAdminAccountRequest:
    out: PutAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if "AdminAccount" in data:
        out["admin_account"] = data["AdminAccount"]
    else:
        raise DeserializationError("PutAdminAccountRequest.admin_account required")
    if "AdminScope" in data:
        import aws_sdk_fms.types.admin_scope

        out["admin_scope"] = aws_sdk_fms.types.admin_scope.deserialize_aws_json_1_1(
            data["AdminScope"]
        )
    return out
