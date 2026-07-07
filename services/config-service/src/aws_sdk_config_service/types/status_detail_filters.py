"""Generated from Smithy shape ``com.amazonaws.configservice#StatusDetailFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.account_id
    import aws_sdk_config_service.types.member_account_rule_status


class StatusDetailFilters(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_config_service.types.account_id.AccountId"]
    """<p>The 12-digit account ID of the member account within an organization.</p>"""
    member_account_rule_status: NotRequired[
        "aws_sdk_config_service.types.member_account_rule_status.MemberAccountRuleStatus"
    ]
    """<p>Indicates deployment status for Config rule in the member account. When management account calls <code>PutOrganizationConfigRule</code> action for the first time, Config rule status is created in the member account. When management account calls <code>PutOrganizationConfigRule</code> action for the second time, Config rule status is updated in the member account. Config rule status is deleted when the management account deletes <code>OrganizationConfigRule</code> and disables service access for <code>config-multiaccountsetup.amazonaws.com</code>. </p> <p>Config sets the state of the rule to:</p> <ul> <li> <p> <code>CREATE_SUCCESSFUL</code> when Config rule has been created in the member account.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> when Config rule is being created in the member account.</p> </li> <li> <p> <code>CREATE_FAILED</code> when Config rule creation has failed in the member account.</p> </li> <li> <p> <code>DELETE_FAILED</code> when Config rule deletion has failed in the member account.</p> </li> <li> <p> <code>DELETE_IN_PROGRESS</code> when Config rule is being deleted in the member account.</p> </li> <li> <p> <code>DELETE_SUCCESSFUL</code> when Config rule has been deleted in the member account.</p> </li> <li> <p> <code>UPDATE_SUCCESSFUL</code> when Config rule has been updated in the member account.</p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> when Config rule is being updated in the member account.</p> </li> <li> <p> <code>UPDATE_FAILED</code> when Config rule deletion has failed in the member account.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatusDetailFilters) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "member_account_rule_status" in value:
        import aws_sdk_config_service.types.member_account_rule_status

        out["MemberAccountRuleStatus"] = (
            aws_sdk_config_service.types.member_account_rule_status.serialize_aws_json_1_1(
                value["member_account_rule_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StatusDetailFilters:
    out: StatusDetailFilters = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "MemberAccountRuleStatus" in data:
        import aws_sdk_config_service.types.member_account_rule_status

        out["member_account_rule_status"] = (
            aws_sdk_config_service.types.member_account_rule_status.deserialize_aws_json_1_1(
                data["MemberAccountRuleStatus"]
            )
        )
    return out
