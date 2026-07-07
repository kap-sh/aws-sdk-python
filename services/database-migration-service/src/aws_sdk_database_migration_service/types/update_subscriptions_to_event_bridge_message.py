"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#UpdateSubscriptionsToEventBridgeMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional


class UpdateSubscriptionsToEventBridgeMessage(TypedDict, closed=True):
    force_move: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When set to true, this operation migrates DMS subscriptions for Amazon SNS notifications no matter what your replication instance version is. If not set or set to false, this operation runs only when all your replication instances are from DMS version 3.4.5 or higher. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSubscriptionsToEventBridgeMessage) -> dict:
    out: dict = {}
    if "force_move" in value:
        out["ForceMove"] = value["force_move"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSubscriptionsToEventBridgeMessage:
    out: UpdateSubscriptionsToEventBridgeMessage = {}  # type: ignore[typeddict-item]
    if "ForceMove" in data:
        out["force_move"] = data["ForceMove"]
    return out
