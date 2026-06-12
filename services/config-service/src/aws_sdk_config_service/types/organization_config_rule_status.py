"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConfigRuleStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.date
    import aws_sdk_config_service.types.organization_config_rule_name
    import aws_sdk_config_service.types.organization_rule_status
    import aws_sdk_config_service.types.string


class OrganizationConfigRuleStatus(TypedDict):
    organization_config_rule_name: "aws_sdk_config_service.types.organization_config_rule_name.OrganizationConfigRuleName"
    """<p>The name that you assign to organization Config rule.</p>"""
    organization_rule_status: (
        "aws_sdk_config_service.types.organization_rule_status.OrganizationRuleStatus"
    )
    """<p>Indicates deployment status of an organization Config rule. When management account calls PutOrganizationConfigRule action for the first time, Config rule status is created in all the member accounts. When management account calls PutOrganizationConfigRule action for the second time, Config rule status is updated in all the member accounts. Additionally, Config rule status is updated when one or more member accounts join or leave an organization. Config rule status is deleted when the management account deletes OrganizationConfigRule in all the member accounts and disables service access for <code>config-multiaccountsetup.amazonaws.com</code>.</p> <p>Config sets the state of the rule to:</p> <ul> <li> <p> <code>CREATE_SUCCESSFUL</code> when an organization Config rule has been successfully created in all the member accounts. </p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> when an organization Config rule creation is in progress.</p> </li> <li> <p> <code>CREATE_FAILED</code> when an organization Config rule creation failed in one or more member accounts within that organization.</p> </li> <li> <p> <code>DELETE_FAILED</code> when an organization Config rule deletion failed in one or more member accounts within that organization.</p> </li> <li> <p> <code>DELETE_IN_PROGRESS</code> when an organization Config rule deletion is in progress.</p> </li> <li> <p> <code>DELETE_SUCCESSFUL</code> when an organization Config rule has been successfully deleted from all the member accounts.</p> </li> <li> <p> <code>UPDATE_SUCCESSFUL</code> when an organization Config rule has been successfully updated in all the member accounts.</p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> when an organization Config rule update is in progress.</p> </li> <li> <p> <code>UPDATE_FAILED</code> when an organization Config rule update failed in one or more member accounts within that organization.</p> </li> </ul>"""
    error_code: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>An error code that is returned when organization Config rule creation or deletion has failed.</p>"""
    error_message: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>An error message indicating that organization Config rule creation or deletion failed due to an error.</p>"""
    last_update_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The timestamp of the last update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConfigRuleStatus) -> dict:
    out: dict = {}
    out["OrganizationConfigRuleName"] = value["organization_config_rule_name"]
    import aws_sdk_config_service.types.organization_rule_status

    out["OrganizationRuleStatus"] = (
        aws_sdk_config_service.types.organization_rule_status.serialize_aws_json_1_1(
            value["organization_rule_status"]
        )
    )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "last_update_time" in value:
        import aws_sdk_config_service.types.date

        out["LastUpdateTime"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["last_update_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationConfigRuleStatus:
    out: OrganizationConfigRuleStatus = {}  # type: ignore[typeddict-item]
    if "OrganizationConfigRuleName" in data:
        out["organization_config_rule_name"] = data["OrganizationConfigRuleName"]
    else:
        raise DeserializationError(
            "OrganizationConfigRuleStatus.organization_config_rule_name required"
        )
    if "OrganizationRuleStatus" in data:
        import aws_sdk_config_service.types.organization_rule_status

        out["organization_rule_status"] = (
            aws_sdk_config_service.types.organization_rule_status.deserialize_aws_json_1_1(
                data["OrganizationRuleStatus"]
            )
        )
    else:
        raise DeserializationError(
            "OrganizationConfigRuleStatus.organization_rule_status required"
        )
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "LastUpdateTime" in data:
        import aws_sdk_config_service.types.date

        out["last_update_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdateTime"]
            )
        )
    return out
