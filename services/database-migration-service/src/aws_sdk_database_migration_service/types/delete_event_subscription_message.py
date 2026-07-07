"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteEventSubscriptionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class DeleteEventSubscriptionMessage(TypedDict, closed=True):
    subscription_name: "aws_sdk_database_migration_service.types.string.String"
    """<p>The name of the DMS event notification subscription to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEventSubscriptionMessage) -> dict:
    out: dict = {}
    out["SubscriptionName"] = value["subscription_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEventSubscriptionMessage:
    out: DeleteEventSubscriptionMessage = {}  # type: ignore[typeddict-item]
    if "SubscriptionName" in data:
        out["subscription_name"] = data["SubscriptionName"]
    else:
        raise DeserializationError(
            "DeleteEventSubscriptionMessage.subscription_name required"
        )
    return out
