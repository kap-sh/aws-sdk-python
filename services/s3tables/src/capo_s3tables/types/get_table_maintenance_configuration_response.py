"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableMaintenanceConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.table_arn
    import capo_s3tables.types.table_maintenance_configuration


class GetTableMaintenanceConfigurationResponse(TypedDict, closed=True):
    table_arn: "capo_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    configuration: "capo_s3tables.types.table_maintenance_configuration.TableMaintenanceConfiguration"
    """<p>Details about the maintenance configuration for the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableMaintenanceConfigurationResponse) -> dict:
    out: dict = {}
    out["tableARN"] = value["table_arn"]
    import capo_s3tables.types.table_maintenance_configuration

    out["configuration"] = (
        capo_s3tables.types.table_maintenance_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTableMaintenanceConfigurationResponse:
    out: GetTableMaintenanceConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "tableARN" in data:
        out["table_arn"] = data["tableARN"]
    else:
        raise DeserializationError(
            "GetTableMaintenanceConfigurationResponse.table_arn required"
        )
    if "configuration" in data:
        import capo_s3tables.types.table_maintenance_configuration

        out["configuration"] = (
            capo_s3tables.types.table_maintenance_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "GetTableMaintenanceConfigurationResponse.configuration required"
        )
    return out
