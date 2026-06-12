"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetMigrationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.migration_id


class GetMigrationRequest(TypedDict):
    migration_id: "aws_sdk_lex_model_building_service.types.migration_id.MigrationId"
    """<p>The unique identifier of the migration to view. The <code>migrationID</code> is returned by the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMigrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMigrationRequest:
    out: GetMigrationRequest = {}  # type: ignore[typeddict-item]
    return out
