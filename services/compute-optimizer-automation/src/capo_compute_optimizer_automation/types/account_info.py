"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AccountInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_compute_optimizer_automation.types.account_id
    import capo_compute_optimizer_automation.types.enrollment_status
    import capo_compute_optimizer_automation.types.organization_rule_mode


class AccountInfo(TypedDict, closed=True):
    account_id: "capo_compute_optimizer_automation.types.account_id.AccountId"
    """<p> The ID of the Amazon Web Services account. </p>"""
    status: "capo_compute_optimizer_automation.types.enrollment_status.EnrollmentStatus"
    """<p> The enrollment status of the account: Active, Inactive, Pending, or Failed. </p>"""
    organization_rule_mode: "capo_compute_optimizer_automation.types.organization_rule_mode.OrganizationRuleMode"
    """<p>Specifies whether the management account can create Automation rules that implement optimization actions for this account. </p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current Automation enrollment status. </p>"""
    last_updated_timestamp: "datetime.datetime"
    """<p>The timestamp when the account's Automation enrollment status was last updated. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountInfo) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import capo_compute_optimizer_automation.types.enrollment_status

    out["status"] = (
        capo_compute_optimizer_automation.types.enrollment_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    import capo_compute_optimizer_automation.types.organization_rule_mode

    out["organizationRuleMode"] = (
        capo_compute_optimizer_automation.types.organization_rule_mode.serialize_aws_json_1_0(
            value["organization_rule_mode"]
        )
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_compute_optimizer_automation.types._prelude.timestamp

    out["lastUpdatedTimestamp"] = (
        capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_updated_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountInfo:
    out: AccountInfo = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("AccountInfo.account_id required")
    if "status" in data:
        import capo_compute_optimizer_automation.types.enrollment_status

        out["status"] = (
            capo_compute_optimizer_automation.types.enrollment_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        raise DeserializationError("AccountInfo.status required")
    if "organizationRuleMode" in data:
        import capo_compute_optimizer_automation.types.organization_rule_mode

        out["organization_rule_mode"] = (
            capo_compute_optimizer_automation.types.organization_rule_mode.deserialize_aws_json_1_0(
                data["organizationRuleMode"]
            )
        )
    else:
        raise DeserializationError("AccountInfo.organization_rule_mode required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "lastUpdatedTimestamp" in data:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedTimestamp"]
            )
        )
    else:
        raise DeserializationError("AccountInfo.last_updated_timestamp required")
    return out
