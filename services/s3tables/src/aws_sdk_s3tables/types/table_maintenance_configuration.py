"""Generated from Smithy shape ``com.amazonaws.s3tables#TableMaintenanceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_maintenance_configuration_value
    import aws_sdk_s3tables.types.table_maintenance_type

TableMaintenanceConfiguration: TypeAlias = dict[
    "aws_sdk_s3tables.types.table_maintenance_type.TableMaintenanceType",
    "aws_sdk_s3tables.types.table_maintenance_configuration_value.TableMaintenanceConfigurationValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TableMaintenanceConfiguration) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_s3tables.types.table_maintenance_configuration_value
        import aws_sdk_s3tables.types.table_maintenance_type

        out[aws_sdk_s3tables.types.table_maintenance_type.serialize_json(key)] = (
            aws_sdk_s3tables.types.table_maintenance_configuration_value.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> TableMaintenanceConfiguration:
    out: TableMaintenanceConfiguration = {}
    for key, value in data.items():
        import aws_sdk_s3tables.types.table_maintenance_configuration_value
        import aws_sdk_s3tables.types.table_maintenance_type

        out[aws_sdk_s3tables.types.table_maintenance_type.deserialize_json(key)] = (
            aws_sdk_s3tables.types.table_maintenance_configuration_value.deserialize_json(
                value
            )
        )
    return out
