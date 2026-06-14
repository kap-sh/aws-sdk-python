"""Generated from Smithy shape ``com.amazonaws.datazone#AssetFilterConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.column_filter_configuration
    import aws_sdk_datazone.types.row_filter_configuration


class _AssetFilterConfiguration_columnConfiguration(TypedDict):
    columnConfiguration: (
        "aws_sdk_datazone.types.column_filter_configuration.ColumnFilterConfiguration"
    )


class _AssetFilterConfiguration_rowConfiguration(TypedDict):
    rowConfiguration: (
        "aws_sdk_datazone.types.row_filter_configuration.RowFilterConfiguration"
    )


AssetFilterConfiguration: TypeAlias = (
    _AssetFilterConfiguration_columnConfiguration
    | _AssetFilterConfiguration_rowConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: AssetFilterConfiguration) -> dict:
    if "columnConfiguration" in value:
        import aws_sdk_datazone.types.column_filter_configuration

        return {
            "columnConfiguration": aws_sdk_datazone.types.column_filter_configuration.serialize_json(
                value["columnConfiguration"]
            )
        }
    elif "rowConfiguration" in value:
        import aws_sdk_datazone.types.row_filter_configuration

        return {
            "rowConfiguration": aws_sdk_datazone.types.row_filter_configuration.serialize_json(
                value["rowConfiguration"]
            )
        }
    else:
        raise SerializationError("AssetFilterConfiguration: no variant present")


def deserialize_json(data: dict) -> AssetFilterConfiguration:
    if "columnConfiguration" in data:
        import aws_sdk_datazone.types.column_filter_configuration

        return {
            "columnConfiguration": aws_sdk_datazone.types.column_filter_configuration.deserialize_json(
                data["columnConfiguration"]
            )
        }
    elif "rowConfiguration" in data:
        import aws_sdk_datazone.types.row_filter_configuration

        return {
            "rowConfiguration": aws_sdk_datazone.types.row_filter_configuration.deserialize_json(
                data["rowConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "AssetFilterConfiguration: no recognized variant key"
        )
