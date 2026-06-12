"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ConfigurationEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.account_id
    import aws_sdk_application_insights.types.configuration_event_detail
    import aws_sdk_application_insights.types.configuration_event_monitored_resource_arn
    import aws_sdk_application_insights.types.configuration_event_resource_name
    import aws_sdk_application_insights.types.configuration_event_resource_type
    import aws_sdk_application_insights.types.configuration_event_status
    import aws_sdk_application_insights.types.configuration_event_time
    import aws_sdk_application_insights.types.resource_group_name


class ConfigurationEvent(TypedDict):
    resource_group_name: NotRequired[
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group of the application to which the configuration event belongs.</p>"""
    account_id: NotRequired["aws_sdk_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the owner of the application to which the configuration event belongs.</p>"""
    monitored_resource_arn: NotRequired[
        "aws_sdk_application_insights.types.configuration_event_monitored_resource_arn.ConfigurationEventMonitoredResourceARN"
    ]
    """<p> The resource monitored by Application Insights. </p>"""
    event_status: NotRequired[
        "aws_sdk_application_insights.types.configuration_event_status.ConfigurationEventStatus"
    ]
    """<p> The status of the configuration update event. Possible values include INFO, WARN, and ERROR. </p>"""
    event_resource_type: NotRequired[
        "aws_sdk_application_insights.types.configuration_event_resource_type.ConfigurationEventResourceType"
    ]
    """<p> The resource type that Application Insights attempted to configure, for example, CLOUDWATCH_ALARM. </p>"""
    event_time: NotRequired[
        "aws_sdk_application_insights.types.configuration_event_time.ConfigurationEventTime"
    ]
    """<p> The timestamp of the event. </p>"""
    event_detail: NotRequired[
        "aws_sdk_application_insights.types.configuration_event_detail.ConfigurationEventDetail"
    ]
    """<p> The details of the event in plain text. </p>"""
    event_resource_name: NotRequired[
        "aws_sdk_application_insights.types.configuration_event_resource_name.ConfigurationEventResourceName"
    ]
    """<p> The name of the resource Application Insights attempted to configure. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationEvent) -> dict:
    out: dict = {}
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "monitored_resource_arn" in value:
        out["MonitoredResourceARN"] = value["monitored_resource_arn"]
    if "event_status" in value:
        import aws_sdk_application_insights.types.configuration_event_status

        out["EventStatus"] = (
            aws_sdk_application_insights.types.configuration_event_status.serialize_aws_json_1_1(
                value["event_status"]
            )
        )
    if "event_resource_type" in value:
        import aws_sdk_application_insights.types.configuration_event_resource_type

        out["EventResourceType"] = (
            aws_sdk_application_insights.types.configuration_event_resource_type.serialize_aws_json_1_1(
                value["event_resource_type"]
            )
        )
    if "event_time" in value:
        import aws_sdk_application_insights.types.configuration_event_time

        out["EventTime"] = (
            aws_sdk_application_insights.types.configuration_event_time.serialize_aws_json_1_1(
                value["event_time"]
            )
        )
    if "event_detail" in value:
        out["EventDetail"] = value["event_detail"]
    if "event_resource_name" in value:
        out["EventResourceName"] = value["event_resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationEvent:
    out: ConfigurationEvent = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "MonitoredResourceARN" in data:
        out["monitored_resource_arn"] = data["MonitoredResourceARN"]
    if "EventStatus" in data:
        import aws_sdk_application_insights.types.configuration_event_status

        out["event_status"] = (
            aws_sdk_application_insights.types.configuration_event_status.deserialize_aws_json_1_1(
                data["EventStatus"]
            )
        )
    if "EventResourceType" in data:
        import aws_sdk_application_insights.types.configuration_event_resource_type

        out["event_resource_type"] = (
            aws_sdk_application_insights.types.configuration_event_resource_type.deserialize_aws_json_1_1(
                data["EventResourceType"]
            )
        )
    if "EventTime" in data:
        import aws_sdk_application_insights.types.configuration_event_time

        out["event_time"] = (
            aws_sdk_application_insights.types.configuration_event_time.deserialize_aws_json_1_1(
                data["EventTime"]
            )
        )
    if "EventDetail" in data:
        out["event_detail"] = data["EventDetail"]
    if "EventResourceName" in data:
        out["event_resource_name"] = data["EventResourceName"]
    return out
