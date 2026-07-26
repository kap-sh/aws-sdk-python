"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.endpoint


class ModifyEndpointResponse(TypedDict, closed=True):
    endpoint: NotRequired["capo_database_migration_service.types.endpoint.Endpoint"]
    """<p>The modified endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint" in value:
        import capo_database_migration_service.types.endpoint

        out["Endpoint"] = (
            capo_database_migration_service.types.endpoint.serialize_aws_json_1_1(
                value["endpoint"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyEndpointResponse:
    out: ModifyEndpointResponse = {}  # type: ignore[typeddict-item]
    if "Endpoint" in data:
        import capo_database_migration_service.types.endpoint

        out["endpoint"] = (
            capo_database_migration_service.types.endpoint.deserialize_aws_json_1_1(
                data["Endpoint"]
            )
        )
    return out
