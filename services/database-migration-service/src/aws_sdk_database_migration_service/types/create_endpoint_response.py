"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.endpoint


class CreateEndpointResponse(TypedDict, closed=True):
    endpoint: NotRequired["aws_sdk_database_migration_service.types.endpoint.Endpoint"]
    """<p>The endpoint that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint" in value:
        import aws_sdk_database_migration_service.types.endpoint

        out["Endpoint"] = (
            aws_sdk_database_migration_service.types.endpoint.serialize_aws_json_1_1(
                value["endpoint"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEndpointResponse:
    out: CreateEndpointResponse = {}  # type: ignore[typeddict-item]
    if "Endpoint" in data:
        import aws_sdk_database_migration_service.types.endpoint

        out["endpoint"] = (
            aws_sdk_database_migration_service.types.endpoint.deserialize_aws_json_1_1(
                data["Endpoint"]
            )
        )
    return out
