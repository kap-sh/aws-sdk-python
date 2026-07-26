"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#TableConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.table_name
    import capo_bcm_data_exports.types.table_properties

TableConfigurations: TypeAlias = dict[
    "capo_bcm_data_exports.types.table_name.TableName",
    "capo_bcm_data_exports.types.table_properties.TableProperties",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TableConfigurations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_bcm_data_exports.types.table_properties

        out[key] = capo_bcm_data_exports.types.table_properties.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TableConfigurations:
    out: TableConfigurations = {}
    for key, value in data.items():
        import capo_bcm_data_exports.types.table_properties

        out[key] = (
            capo_bcm_data_exports.types.table_properties.deserialize_aws_json_1_1(value)
        )
    return out
