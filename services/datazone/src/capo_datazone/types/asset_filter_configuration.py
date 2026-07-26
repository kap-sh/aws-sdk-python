"""Generated from Smithy shape ``com.amazonaws.datazone#AssetFilterConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.column_filter_configuration
    import capo_datazone.types.row_filter_configuration


class _AssetFilterConfiguration_columnConfiguration(TypedDict, closed=True):
    columnConfiguration: (
        "capo_datazone.types.column_filter_configuration.ColumnFilterConfiguration"
    )


class _AssetFilterConfiguration_rowConfiguration(TypedDict, closed=True):
    rowConfiguration: (
        "capo_datazone.types.row_filter_configuration.RowFilterConfiguration"
    )


AssetFilterConfiguration: TypeAlias = (
    _AssetFilterConfiguration_columnConfiguration
    | _AssetFilterConfiguration_rowConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: AssetFilterConfiguration) -> dict:
    if "columnConfiguration" in value:
        import capo_datazone.types.column_filter_configuration

        return {
            "columnConfiguration": capo_datazone.types.column_filter_configuration.serialize_json(
                value["columnConfiguration"]
            )
        }
    elif "rowConfiguration" in value:
        import capo_datazone.types.row_filter_configuration

        return {
            "rowConfiguration": capo_datazone.types.row_filter_configuration.serialize_json(
                value["rowConfiguration"]
            )
        }
    else:
        raise SerializationError("AssetFilterConfiguration: no variant present")


def deserialize_json(data: dict) -> AssetFilterConfiguration:
    if "columnConfiguration" in data:
        import capo_datazone.types.column_filter_configuration

        return {
            "columnConfiguration": capo_datazone.types.column_filter_configuration.deserialize_json(
                data["columnConfiguration"]
            )
        }
    elif "rowConfiguration" in data:
        import capo_datazone.types.row_filter_configuration

        return {
            "rowConfiguration": capo_datazone.types.row_filter_configuration.deserialize_json(
                data["rowConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "AssetFilterConfiguration: no recognized variant key"
        )
