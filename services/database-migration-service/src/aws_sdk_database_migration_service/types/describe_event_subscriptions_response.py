"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeEventSubscriptionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.event_subscriptions_list
    import aws_sdk_database_migration_service.types.string


class DescribeEventSubscriptionsResponse(TypedDict):
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    event_subscriptions_list: NotRequired[
        "aws_sdk_database_migration_service.types.event_subscriptions_list.EventSubscriptionsList"
    ]
    """<p>A list of event subscriptions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventSubscriptionsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "event_subscriptions_list" in value:
        import aws_sdk_database_migration_service.types.event_subscriptions_list

        out["EventSubscriptionsList"] = (
            aws_sdk_database_migration_service.types.event_subscriptions_list.serialize_aws_json_1_1(
                value["event_subscriptions_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventSubscriptionsResponse:
    out: DescribeEventSubscriptionsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "EventSubscriptionsList" in data:
        import aws_sdk_database_migration_service.types.event_subscriptions_list

        out["event_subscriptions_list"] = (
            aws_sdk_database_migration_service.types.event_subscriptions_list.deserialize_aws_json_1_1(
                data["EventSubscriptionsList"]
            )
        )
    return out
