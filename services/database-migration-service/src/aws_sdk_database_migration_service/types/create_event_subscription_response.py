"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateEventSubscriptionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.event_subscription


class CreateEventSubscriptionResponse(TypedDict):
    event_subscription: NotRequired[
        "aws_sdk_database_migration_service.types.event_subscription.EventSubscription"
    ]
    """<p>The event subscription that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEventSubscriptionResponse) -> dict:
    out: dict = {}
    if "event_subscription" in value:
        import aws_sdk_database_migration_service.types.event_subscription

        out["EventSubscription"] = (
            aws_sdk_database_migration_service.types.event_subscription.serialize_aws_json_1_1(
                value["event_subscription"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEventSubscriptionResponse:
    out: CreateEventSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "EventSubscription" in data:
        import aws_sdk_database_migration_service.types.event_subscription

        out["event_subscription"] = (
            aws_sdk_database_migration_service.types.event_subscription.deserialize_aws_json_1_1(
                data["EventSubscription"]
            )
        )
    return out
