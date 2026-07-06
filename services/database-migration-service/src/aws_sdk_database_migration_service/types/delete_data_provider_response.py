"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteDataProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.data_provider


class DeleteDataProviderResponse(TypedDict, closed=True):
    data_provider: NotRequired[
        "aws_sdk_database_migration_service.types.data_provider.DataProvider"
    ]
    """<p>The data provider that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDataProviderResponse) -> dict:
    out: dict = {}
    if "data_provider" in value:
        import aws_sdk_database_migration_service.types.data_provider

        out["DataProvider"] = (
            aws_sdk_database_migration_service.types.data_provider.serialize_aws_json_1_1(
                value["data_provider"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDataProviderResponse:
    out: DeleteDataProviderResponse = {}  # type: ignore[typeddict-item]
    if "DataProvider" in data:
        import aws_sdk_database_migration_service.types.data_provider

        out["data_provider"] = (
            aws_sdk_database_migration_service.types.data_provider.deserialize_aws_json_1_1(
                data["DataProvider"]
            )
        )
    return out
