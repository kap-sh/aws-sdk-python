"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CollectorShortInfoResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class CollectorShortInfoResponse(TypedDict, closed=True):
    collector_referenced_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The reference ID of the Fleet Advisor collector.</p>"""
    collector_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the Fleet Advisor collector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollectorShortInfoResponse) -> dict:
    out: dict = {}
    if "collector_referenced_id" in value:
        out["CollectorReferencedId"] = value["collector_referenced_id"]
    if "collector_name" in value:
        out["CollectorName"] = value["collector_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CollectorShortInfoResponse:
    out: CollectorShortInfoResponse = {}  # type: ignore[typeddict-item]
    if "CollectorReferencedId" in data:
        out["collector_referenced_id"] = data["CollectorReferencedId"]
    if "CollectorName" in data:
        out["collector_name"] = data["CollectorName"]
    return out
