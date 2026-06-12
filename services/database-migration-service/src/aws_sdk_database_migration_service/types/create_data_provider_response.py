"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateDataProviderResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.data_provider


class CreateDataProviderResponse(TypedDict):
    data_provider: NotRequired[
        "aws_sdk_database_migration_service.types.data_provider.DataProvider"
    ]
    """<p>The data provider that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataProviderResponse) -> dict:
    out: dict = {}
    if "data_provider" in value:
        import aws_sdk_database_migration_service.types.data_provider

        out["DataProvider"] = (
            aws_sdk_database_migration_service.types.data_provider.serialize_aws_json_1_1(
                value["data_provider"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataProviderResponse:
    out: CreateDataProviderResponse = {}  # type: ignore[typeddict-item]
    if "DataProvider" in data:
        import aws_sdk_database_migration_service.types.data_provider

        out["data_provider"] = (
            aws_sdk_database_migration_service.types.data_provider.deserialize_aws_json_1_1(
                data["DataProvider"]
            )
        )
    return out
