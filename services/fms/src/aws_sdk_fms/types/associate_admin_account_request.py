"""Generated from Smithy shape ``com.amazonaws.fms#AssociateAdminAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.aws_account_id


class AssociateAdminAccountRequest(TypedDict):
    admin_account: "aws_sdk_fms.types.aws_account_id.AWSAccountId"
    """<p>The Amazon Web Services account ID to associate with Firewall Manager as the Firewall Manager default administrator account. This account must be a member account of the organization in Organizations whose resources you want to protect. For more information about Organizations, see <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html\">Managing the Amazon Web Services Accounts in Your Organization</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateAdminAccountRequest) -> dict:
    out: dict = {}
    out["AdminAccount"] = value["admin_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateAdminAccountRequest:
    out: AssociateAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if "AdminAccount" in data:
        out["admin_account"] = data["AdminAccount"]
    else:
        raise DeserializationError(
            "AssociateAdminAccountRequest.admin_account required"
        )
    return out
