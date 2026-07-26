"""Generated from Smithy shape ``com.amazonaws.s3tables#PutTableMaintenanceConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_maintenance_configuration_value
    import capo_s3tables.types.table_maintenance_type
    import capo_s3tables.types.table_name


class PutTableMaintenanceConfigurationRequest(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table associated with the maintenance configuration.</p>"""
    namespace: "capo_s3tables.types.namespace_name.NamespaceName"
    """<p>The namespace of the table.</p>"""
    name: "capo_s3tables.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    type: "capo_s3tables.types.table_maintenance_type.TableMaintenanceType"
    """<p>The type of the maintenance configuration.</p>"""
    value: "capo_s3tables.types.table_maintenance_configuration_value.TableMaintenanceConfigurationValue"
    """<p>Defines the values of the maintenance configuration for the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTableMaintenanceConfigurationRequest) -> dict:
    out: dict = {}
    import capo_s3tables.types.table_maintenance_configuration_value

    out["value"] = (
        capo_s3tables.types.table_maintenance_configuration_value.serialize_json(
            value["value"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutTableMaintenanceConfigurationRequest:
    out: PutTableMaintenanceConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "value" in data:
        import capo_s3tables.types.table_maintenance_configuration_value

        out["value"] = (
            capo_s3tables.types.table_maintenance_configuration_value.deserialize_json(
                data["value"]
            )
        )
    else:
        raise DeserializationError(
            "PutTableMaintenanceConfigurationRequest.value required"
        )
    return out
