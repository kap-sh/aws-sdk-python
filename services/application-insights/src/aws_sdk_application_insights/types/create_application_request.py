"""Generated from Smithy shape ``com.amazonaws.applicationinsights#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.attach_missing_permission
    import aws_sdk_application_insights.types.auto_config_enabled
    import aws_sdk_application_insights.types.auto_create
    import aws_sdk_application_insights.types.cwe_monitor_enabled
    import aws_sdk_application_insights.types.grouping_type
    import aws_sdk_application_insights.types.ops_center_enabled
    import aws_sdk_application_insights.types.ops_item_sns_topic_arn
    import aws_sdk_application_insights.types.resource_group_name
    import aws_sdk_application_insights.types.sns_notification_arn
    import aws_sdk_application_insights.types.tag_list


class CreateApplicationRequest(TypedDict, closed=True):
    resource_group_name: NotRequired[
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group.</p>"""
    ops_center_enabled: NotRequired[
        "aws_sdk_application_insights.types.ops_center_enabled.OpsCenterEnabled"
    ]
    """<p> When set to <code>true</code>, creates opsItems for any problems detected on an application. </p>"""
    cwe_monitor_enabled: NotRequired[
        "aws_sdk_application_insights.types.cwe_monitor_enabled.CWEMonitorEnabled"
    ]
    """<p> Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as <code>instance terminated</code>, <code>failed deployment</code>, and others. </p>"""
    ops_item_sns_topic_arn: NotRequired[
        "aws_sdk_application_insights.types.ops_item_sns_topic_arn.OpsItemSNSTopicArn"
    ]
    """<p> The SNS topic provided to Application Insights that is associated to the created opsItem. Allows you to receive notifications for updates to the opsItem. </p>"""
    sns_notification_arn: NotRequired[
        "aws_sdk_application_insights.types.sns_notification_arn.SNSNotificationArn"
    ]
    """<p> The SNS notification topic ARN. </p>"""
    tags: NotRequired["aws_sdk_application_insights.types.tag_list.TagList"]
    """<p>List of tags to add to the application. tag key (<code>Key</code>) and an associated tag value (<code>Value</code>). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>"""
    auto_config_enabled: NotRequired[
        "aws_sdk_application_insights.types.auto_config_enabled.AutoConfigEnabled"
    ]
    """<p> Indicates whether Application Insights automatically configures unmonitored resources in the resource group. </p>"""
    auto_create: NotRequired[
        "aws_sdk_application_insights.types.auto_create.AutoCreate"
    ]
    """<p> Configures all of the resources in the resource group by applying the recommended configurations. </p>"""
    grouping_type: NotRequired[
        "aws_sdk_application_insights.types.grouping_type.GroupingType"
    ]
    """<p>Application Insights can create applications based on a resource group or on an account. To create an account-based application using all of the resources in the account, set this parameter to <code>ACCOUNT_BASED</code>. </p>"""
    attach_missing_permission: NotRequired[
        "aws_sdk_application_insights.types.attach_missing_permission.AttachMissingPermission"
    ]
    """<p>If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "ops_center_enabled" in value:
        out["OpsCenterEnabled"] = value["ops_center_enabled"]
    if "cwe_monitor_enabled" in value:
        out["CWEMonitorEnabled"] = value["cwe_monitor_enabled"]
    if "ops_item_sns_topic_arn" in value:
        out["OpsItemSNSTopicArn"] = value["ops_item_sns_topic_arn"]
    if "sns_notification_arn" in value:
        out["SNSNotificationArn"] = value["sns_notification_arn"]
    if "tags" in value:
        import aws_sdk_application_insights.types.tag_list

        out["Tags"] = (
            aws_sdk_application_insights.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    if "auto_config_enabled" in value:
        out["AutoConfigEnabled"] = value["auto_config_enabled"]
    if "auto_create" in value:
        out["AutoCreate"] = value["auto_create"]
    if "grouping_type" in value:
        import aws_sdk_application_insights.types.grouping_type

        out["GroupingType"] = (
            aws_sdk_application_insights.types.grouping_type.serialize_aws_json_1_1(
                value["grouping_type"]
            )
        )
    if "attach_missing_permission" in value:
        out["AttachMissingPermission"] = value["attach_missing_permission"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    if "OpsCenterEnabled" in data:
        out["ops_center_enabled"] = data["OpsCenterEnabled"]
    if "CWEMonitorEnabled" in data:
        out["cwe_monitor_enabled"] = data["CWEMonitorEnabled"]
    if "OpsItemSNSTopicArn" in data:
        out["ops_item_sns_topic_arn"] = data["OpsItemSNSTopicArn"]
    if "SNSNotificationArn" in data:
        out["sns_notification_arn"] = data["SNSNotificationArn"]
    if "Tags" in data:
        import aws_sdk_application_insights.types.tag_list

        out["tags"] = (
            aws_sdk_application_insights.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    if "AutoConfigEnabled" in data:
        out["auto_config_enabled"] = data["AutoConfigEnabled"]
    if "AutoCreate" in data:
        out["auto_create"] = data["AutoCreate"]
    if "GroupingType" in data:
        import aws_sdk_application_insights.types.grouping_type

        out["grouping_type"] = (
            aws_sdk_application_insights.types.grouping_type.deserialize_aws_json_1_1(
                data["GroupingType"]
            )
        )
    if "AttachMissingPermission" in data:
        out["attach_missing_permission"] = data["AttachMissingPermission"]
    return out
