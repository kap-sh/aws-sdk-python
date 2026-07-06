"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EventSubscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean
    import aws_sdk_database_migration_service.types.event_categories_list
    import aws_sdk_database_migration_service.types.source_ids_list
    import aws_sdk_database_migration_service.types.string


class EventSubscription(TypedDict, closed=True):
    customer_aws_id: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Web Services customer account associated with the DMS event notification subscription.</p>"""
    cust_subscription_id: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The DMS event notification subscription Id.</p>"""
    sns_topic_arn: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The topic ARN of the DMS event notification subscription.</p>"""
    status: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    r"""<p>The status of the DMS event notification subscription.</p> <p>Constraints:</p> <p>Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist</p> <p>The status \"no-permission\" indicates that DMS no longer has permission to post to the SNS topic. The status \"topic-not-exist\" indicates that the topic was deleted after the subscription was created.</p>"""
    subscription_creation_time: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The time the DMS event notification subscription was created.</p>"""
    source_type: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p> The type of DMS resource that generates events. </p> <p>Valid values: replication-instance | replication-server | security-group | replication-task</p>"""
    source_ids_list: NotRequired[
        "aws_sdk_database_migration_service.types.source_ids_list.SourceIdsList"
    ]
    """<p>A list of source Ids for the event subscription.</p>"""
    event_categories_list: NotRequired[
        "aws_sdk_database_migration_service.types.event_categories_list.EventCategoriesList"
    ]
    """<p>A lists of event categories.</p>"""
    enabled: "aws_sdk_database_migration_service.types.boolean.Boolean"
    """<p>Boolean value that indicates if the event subscription is enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventSubscription) -> dict:
    out: dict = {}
    if "customer_aws_id" in value:
        out["CustomerAwsId"] = value["customer_aws_id"]
    if "cust_subscription_id" in value:
        out["CustSubscriptionId"] = value["cust_subscription_id"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "status" in value:
        out["Status"] = value["status"]
    if "subscription_creation_time" in value:
        out["SubscriptionCreationTime"] = value["subscription_creation_time"]
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "source_ids_list" in value:
        import aws_sdk_database_migration_service.types.source_ids_list

        out["SourceIdsList"] = (
            aws_sdk_database_migration_service.types.source_ids_list.serialize_aws_json_1_1(
                value["source_ids_list"]
            )
        )
    if "event_categories_list" in value:
        import aws_sdk_database_migration_service.types.event_categories_list

        out["EventCategoriesList"] = (
            aws_sdk_database_migration_service.types.event_categories_list.serialize_aws_json_1_1(
                value["event_categories_list"]
            )
        )
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> EventSubscription:
    out: EventSubscription = {}  # type: ignore[typeddict-item]
    if "CustomerAwsId" in data:
        out["customer_aws_id"] = data["CustomerAwsId"]
    if "CustSubscriptionId" in data:
        out["cust_subscription_id"] = data["CustSubscriptionId"]
    if "SnsTopicArn" in data:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "SubscriptionCreationTime" in data:
        out["subscription_creation_time"] = data["SubscriptionCreationTime"]
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    if "SourceIdsList" in data:
        import aws_sdk_database_migration_service.types.source_ids_list

        out["source_ids_list"] = (
            aws_sdk_database_migration_service.types.source_ids_list.deserialize_aws_json_1_1(
                data["SourceIdsList"]
            )
        )
    if "EventCategoriesList" in data:
        import aws_sdk_database_migration_service.types.event_categories_list

        out["event_categories_list"] = (
            aws_sdk_database_migration_service.types.event_categories_list.deserialize_aws_json_1_1(
                data["EventCategoriesList"]
            )
        )
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
