"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyDataProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.data_provider


class ModifyDataProviderResponse(TypedDict, closed=True):
    data_provider: NotRequired[
        "capo_database_migration_service.types.data_provider.DataProvider"
    ]
    """<p>The data provider that was modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyDataProviderResponse) -> dict:
    out: dict = {}
    if "data_provider" in value:
        import capo_database_migration_service.types.data_provider

        out["DataProvider"] = (
            capo_database_migration_service.types.data_provider.serialize_aws_json_1_1(
                value["data_provider"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyDataProviderResponse:
    out: ModifyDataProviderResponse = {}  # type: ignore[typeddict-item]
    if "DataProvider" in data:
        import capo_database_migration_service.types.data_provider

        out["data_provider"] = (
            capo_database_migration_service.types.data_provider.deserialize_aws_json_1_1(
                data["DataProvider"]
            )
        )
    return out
