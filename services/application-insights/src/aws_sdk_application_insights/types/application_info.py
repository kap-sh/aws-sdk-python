"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ApplicationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.account_id
    import aws_sdk_application_insights.types.attach_missing_permission
    import aws_sdk_application_insights.types.auto_config_enabled
    import aws_sdk_application_insights.types.cwe_monitor_enabled
    import aws_sdk_application_insights.types.discovery_type
    import aws_sdk_application_insights.types.life_cycle
    import aws_sdk_application_insights.types.ops_center_enabled
    import aws_sdk_application_insights.types.ops_item_sns_topic_arn
    import aws_sdk_application_insights.types.remarks
    import aws_sdk_application_insights.types.resource_group_name
    import aws_sdk_application_insights.types.sns_notification_arn


class ApplicationInfo(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the owner of the application.</p>"""
    resource_group_name: NotRequired[
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group used for the application.</p>"""
    life_cycle: NotRequired["aws_sdk_application_insights.types.life_cycle.LifeCycle"]
    """<p>The lifecycle of the application. </p>"""
    ops_item_sns_topic_arn: NotRequired[
        "aws_sdk_application_insights.types.ops_item_sns_topic_arn.OpsItemSNSTopicArn"
    ]
    """<p> The SNS topic provided to Application Insights that is associated to the created opsItems to receive SNS notifications for opsItem updates. </p>"""
    sns_notification_arn: NotRequired[
        "aws_sdk_application_insights.types.sns_notification_arn.SNSNotificationArn"
    ]
    """<p> The SNS topic ARN that is associated with SNS notifications for updates or issues. </p>"""
    ops_center_enabled: NotRequired[
        "aws_sdk_application_insights.types.ops_center_enabled.OpsCenterEnabled"
    ]
    """<p> Indicates whether Application Insights will create opsItems for any problem detected by Application Insights for an application. </p>"""
    cwe_monitor_enabled: NotRequired[
        "aws_sdk_application_insights.types.cwe_monitor_enabled.CWEMonitorEnabled"
    ]
    """<p> Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as <code>instance terminated</code>, <code>failed deployment</code>, and others. </p>"""
    remarks: NotRequired["aws_sdk_application_insights.types.remarks.Remarks"]
    """<p>The issues on the user side that block Application Insights from successfully monitoring an application. Example remarks include:</p> <ul> <li> <p>“Configuring application, detected 1 Errors, 3 Warnings”</p> </li> <li> <p>“Configuring application, detected 1 Unconfigured Components”</p> </li> </ul>"""
    auto_config_enabled: NotRequired[
        "aws_sdk_application_insights.types.auto_config_enabled.AutoConfigEnabled"
    ]
    """<p> Indicates whether auto-configuration is turned on for this application. </p>"""
    discovery_type: NotRequired[
        "aws_sdk_application_insights.types.discovery_type.DiscoveryType"
    ]
    """<p> The method used by Application Insights to onboard your resources. </p>"""
    attach_missing_permission: NotRequired[
        "aws_sdk_application_insights.types.attach_missing_permission.AttachMissingPermission"
    ]
    """<p>If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationInfo) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "life_cycle" in value:
        out["LifeCycle"] = value["life_cycle"]
    if "ops_item_sns_topic_arn" in value:
        out["OpsItemSNSTopicArn"] = value["ops_item_sns_topic_arn"]
    if "sns_notification_arn" in value:
        out["SNSNotificationArn"] = value["sns_notification_arn"]
    if "ops_center_enabled" in value:
        out["OpsCenterEnabled"] = value["ops_center_enabled"]
    if "cwe_monitor_enabled" in value:
        out["CWEMonitorEnabled"] = value["cwe_monitor_enabled"]
    if "remarks" in value:
        out["Remarks"] = value["remarks"]
    if "auto_config_enabled" in value:
        out["AutoConfigEnabled"] = value["auto_config_enabled"]
    if "discovery_type" in value:
        import aws_sdk_application_insights.types.discovery_type

        out["DiscoveryType"] = (
            aws_sdk_application_insights.types.discovery_type.serialize_aws_json_1_1(
                value["discovery_type"]
            )
        )
    if "attach_missing_permission" in value:
        out["AttachMissingPermission"] = value["attach_missing_permission"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationInfo:
    out: ApplicationInfo = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    if "LifeCycle" in data:
        out["life_cycle"] = data["LifeCycle"]
    if "OpsItemSNSTopicArn" in data:
        out["ops_item_sns_topic_arn"] = data["OpsItemSNSTopicArn"]
    if "SNSNotificationArn" in data:
        out["sns_notification_arn"] = data["SNSNotificationArn"]
    if "OpsCenterEnabled" in data:
        out["ops_center_enabled"] = data["OpsCenterEnabled"]
    if "CWEMonitorEnabled" in data:
        out["cwe_monitor_enabled"] = data["CWEMonitorEnabled"]
    if "Remarks" in data:
        out["remarks"] = data["Remarks"]
    if "AutoConfigEnabled" in data:
        out["auto_config_enabled"] = data["AutoConfigEnabled"]
    if "DiscoveryType" in data:
        import aws_sdk_application_insights.types.discovery_type

        out["discovery_type"] = (
            aws_sdk_application_insights.types.discovery_type.deserialize_aws_json_1_1(
                data["DiscoveryType"]
            )
        )
    if "AttachMissingPermission" in data:
        out["attach_missing_permission"] = data["AttachMissingPermission"]
    return out
