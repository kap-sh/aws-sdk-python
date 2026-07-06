"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#InventoryData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.integer_optional


class InventoryData(TypedDict, closed=True):
    number_of_databases: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of databases in the Fleet Advisor collector inventory.</p>"""
    number_of_schemas: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of schemas in the Fleet Advisor collector inventory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryData) -> dict:
    out: dict = {}
    if "number_of_databases" in value:
        out["NumberOfDatabases"] = value["number_of_databases"]
    if "number_of_schemas" in value:
        out["NumberOfSchemas"] = value["number_of_schemas"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryData:
    out: InventoryData = {}  # type: ignore[typeddict-item]
    if "NumberOfDatabases" in data:
        out["number_of_databases"] = data["NumberOfDatabases"]
    if "NumberOfSchemas" in data:
        out["number_of_schemas"] = data["NumberOfSchemas"]
    return out
