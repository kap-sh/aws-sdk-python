"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CancelMetadataModelCreationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.schema_conversion_request


class CancelMetadataModelCreationResponse(TypedDict, closed=True):
    request: NotRequired[
        "capo_database_migration_service.types.schema_conversion_request.SchemaConversionRequest"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelMetadataModelCreationResponse) -> dict:
    out: dict = {}
    if "request" in value:
        import capo_database_migration_service.types.schema_conversion_request

        out["Request"] = (
            capo_database_migration_service.types.schema_conversion_request.serialize_aws_json_1_1(
                value["request"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelMetadataModelCreationResponse:
    out: CancelMetadataModelCreationResponse = {}  # type: ignore[typeddict-item]
    if "Request" in data:
        import capo_database_migration_service.types.schema_conversion_request

        out["request"] = (
            capo_database_migration_service.types.schema_conversion_request.deserialize_aws_json_1_1(
                data["Request"]
            )
        )
    return out
