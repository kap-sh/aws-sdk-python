"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartMetadataModelCreationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class StartMetadataModelCreationResponse(TypedDict, closed=True):
    request_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The identifier for the metadata model creation operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMetadataModelCreationResponse) -> dict:
    out: dict = {}
    if "request_identifier" in value:
        out["RequestIdentifier"] = value["request_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMetadataModelCreationResponse:
    out: StartMetadataModelCreationResponse = {}  # type: ignore[typeddict-item]
    if "RequestIdentifier" in data:
        out["request_identifier"] = data["RequestIdentifier"]
    return out
