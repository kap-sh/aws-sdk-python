"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DefaultErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DefaultErrorDetails(TypedDict, closed=True):
    message: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultErrorDetails) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DefaultErrorDetails:
    out: DefaultErrorDetails = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
