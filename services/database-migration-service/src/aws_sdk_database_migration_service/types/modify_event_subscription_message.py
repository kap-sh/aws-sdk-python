"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyEventSubscriptionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.event_categories_list
    import aws_sdk_database_migration_service.types.string


class ModifyEventSubscriptionMessage(TypedDict):
    subscription_name: "aws_sdk_database_migration_service.types.string.String"
    """<p>The name of the DMS event notification subscription to be modified.</p>"""
    sns_topic_arn: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p> The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.</p>"""
    source_type: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p> The type of DMS resource that generates the events you want to subscribe to. </p> <p>Valid values: replication-instance | replication-task</p>"""
    event_categories: NotRequired[
        "aws_sdk_database_migration_service.types.event_categories_list.EventCategoriesList"
    ]
    """<p> A list of event categories for a source type that you want to subscribe to. Use the <code>DescribeEventCategories</code> action to see a list of event categories. </p>"""
    enabled: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p> A Boolean value; set to <b>true</b> to activate the subscription. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyEventSubscriptionMessage) -> dict:
    out: dict = {}
    out["SubscriptionName"] = value["subscription_name"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "event_categories" in value:
        import aws_sdk_database_migration_service.types.event_categories_list

        out["EventCategories"] = (
            aws_sdk_database_migration_service.types.event_categories_list.serialize_aws_json_1_1(
                value["event_categories"]
            )
        )
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyEventSubscriptionMessage:
    out: ModifyEventSubscriptionMessage = {}  # type: ignore[typeddict-item]
    if "SubscriptionName" in data:
        out["subscription_name"] = data["SubscriptionName"]
    else:
        raise DeserializationError(
            "ModifyEventSubscriptionMessage.subscription_name required"
        )
    if "SnsTopicArn" in data:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    if "EventCategories" in data:
        import aws_sdk_database_migration_service.types.event_categories_list

        out["event_categories"] = (
            aws_sdk_database_migration_service.types.event_categories_list.deserialize_aws_json_1_1(
                data["EventCategories"]
            )
        )
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
