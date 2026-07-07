"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationDefinitionsRequestFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_defintions_i_ds_filter


class ListNetworkMigrationDefinitionsRequestFilters(TypedDict, closed=True):
    network_migration_definition_i_ds: NotRequired[
        "aws_sdk_mgn.types.network_migration_defintions_i_ds_filter.NetworkMigrationDefintionsIDsFilter"
    ]
    """<p>A list of definition IDs to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationDefinitionsRequestFilters) -> dict:
    out: dict = {}
    if "network_migration_definition_i_ds" in value:
        import aws_sdk_mgn.types.network_migration_defintions_i_ds_filter

        out["networkMigrationDefinitionIDs"] = (
            aws_sdk_mgn.types.network_migration_defintions_i_ds_filter.serialize_json(
                value["network_migration_definition_i_ds"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationDefinitionsRequestFilters:
    out: ListNetworkMigrationDefinitionsRequestFilters = {}  # type: ignore[typeddict-item]
    if "networkMigrationDefinitionIDs" in data:
        import aws_sdk_mgn.types.network_migration_defintions_i_ds_filter

        out["network_migration_definition_i_ds"] = (
            aws_sdk_mgn.types.network_migration_defintions_i_ds_filter.deserialize_json(
                data["networkMigrationDefinitionIDs"]
            )
        )
    return out
