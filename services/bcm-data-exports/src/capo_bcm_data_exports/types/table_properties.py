"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#TableProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.table_property
    import capo_bcm_data_exports.types.table_property_generic_string

TableProperties: TypeAlias = dict[
    "capo_bcm_data_exports.types.table_property.TableProperty",
    "capo_bcm_data_exports.types.table_property_generic_string.TablePropertyGenericString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TableProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> TableProperties:
    out: TableProperties = {}
    for key, value in data.items():
        out[key] = value
    return out
