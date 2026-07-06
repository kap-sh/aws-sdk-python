"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AvailabilityZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class AvailabilityZone(TypedDict, closed=True):
    name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The name of the Availability Zone.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailabilityZone) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AvailabilityZone:
    out: AvailabilityZone = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
