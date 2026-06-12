"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.endpoint


class DeleteEndpointResponse(TypedDict):
    endpoint: NotRequired["aws_sdk_database_migration_service.types.endpoint.Endpoint"]
    """<p>The endpoint that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint" in value:
        import aws_sdk_database_migration_service.types.endpoint

        out["Endpoint"] = (
            aws_sdk_database_migration_service.types.endpoint.serialize_aws_json_1_1(
                value["endpoint"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEndpointResponse:
    out: DeleteEndpointResponse = {}  # type: ignore[typeddict-item]
    if "Endpoint" in data:
        import aws_sdk_database_migration_service.types.endpoint

        out["endpoint"] = (
            aws_sdk_database_migration_service.types.endpoint.deserialize_aws_json_1_1(
                data["Endpoint"]
            )
        )
    return out
