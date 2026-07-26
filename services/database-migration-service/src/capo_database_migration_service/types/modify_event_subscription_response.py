"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyEventSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.event_subscription


class ModifyEventSubscriptionResponse(TypedDict, closed=True):
    event_subscription: NotRequired[
        "capo_database_migration_service.types.event_subscription.EventSubscription"
    ]
    """<p>The modified event subscription.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyEventSubscriptionResponse) -> dict:
    out: dict = {}
    if "event_subscription" in value:
        import capo_database_migration_service.types.event_subscription

        out["EventSubscription"] = (
            capo_database_migration_service.types.event_subscription.serialize_aws_json_1_1(
                value["event_subscription"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyEventSubscriptionResponse:
    out: ModifyEventSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "EventSubscription" in data:
        import capo_database_migration_service.types.event_subscription

        out["event_subscription"] = (
            capo_database_migration_service.types.event_subscription.deserialize_aws_json_1_1(
                data["EventSubscription"]
            )
        )
    return out
