"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CancelMetadataModelConversionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.schema_conversion_request


class CancelMetadataModelConversionResponse(TypedDict):
    request: NotRequired[
        "aws_sdk_database_migration_service.types.schema_conversion_request.SchemaConversionRequest"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelMetadataModelConversionResponse) -> dict:
    out: dict = {}
    if "request" in value:
        import aws_sdk_database_migration_service.types.schema_conversion_request

        out["Request"] = (
            aws_sdk_database_migration_service.types.schema_conversion_request.serialize_aws_json_1_1(
                value["request"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelMetadataModelConversionResponse:
    out: CancelMetadataModelConversionResponse = {}  # type: ignore[typeddict-item]
    if "Request" in data:
        import aws_sdk_database_migration_service.types.schema_conversion_request

        out["request"] = (
            aws_sdk_database_migration_service.types.schema_conversion_request.deserialize_aws_json_1_1(
                data["Request"]
            )
        )
    return out
