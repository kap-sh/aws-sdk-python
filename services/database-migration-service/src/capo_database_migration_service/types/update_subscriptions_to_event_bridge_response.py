"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#UpdateSubscriptionsToEventBridgeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class UpdateSubscriptionsToEventBridgeResponse(TypedDict, closed=True):
    result: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A string that indicates how many event subscriptions were migrated and how many remain to be migrated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSubscriptionsToEventBridgeResponse) -> dict:
    out: dict = {}
    if "result" in value:
        out["Result"] = value["result"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSubscriptionsToEventBridgeResponse:
    out: UpdateSubscriptionsToEventBridgeResponse = {}  # type: ignore[typeddict-item]
    if "Result" in data:
        out["result"] = data["Result"]
    return out
