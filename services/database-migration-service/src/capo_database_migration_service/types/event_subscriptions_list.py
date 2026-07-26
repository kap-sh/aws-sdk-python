"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EventSubscriptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.event_subscription

EventSubscriptionsList: TypeAlias = list[
    "capo_database_migration_service.types.event_subscription.EventSubscription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventSubscriptionsList) -> list:
    import capo_database_migration_service.types.event_subscription

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.event_subscription.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventSubscriptionsList:
    import capo_database_migration_service.types.event_subscription

    out: EventSubscriptionsList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.event_subscription.deserialize_aws_json_1_1(
                item
            )
        )
    return out
