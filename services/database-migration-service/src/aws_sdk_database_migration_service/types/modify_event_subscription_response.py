"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyEventSubscriptionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.event_subscription


class ModifyEventSubscriptionResponse(TypedDict):
    event_subscription: NotRequired[
        "aws_sdk_database_migration_service.types.event_subscription.EventSubscription"
    ]
    """<p>The modified event subscription.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyEventSubscriptionResponse) -> dict:
    out: dict = {}
    if "event_subscription" in value:
        import aws_sdk_database_migration_service.types.event_subscription

        out["EventSubscription"] = (
            aws_sdk_database_migration_service.types.event_subscription.serialize_aws_json_1_1(
                value["event_subscription"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyEventSubscriptionResponse:
    out: ModifyEventSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "EventSubscription" in data:
        import aws_sdk_database_migration_service.types.event_subscription

        out["event_subscription"] = (
            aws_sdk_database_migration_service.types.event_subscription.deserialize_aws_json_1_1(
                data["EventSubscription"]
            )
        )
    return out
