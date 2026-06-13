"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#TablePropertyDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.table_property_description

TablePropertyDescriptionList: TypeAlias = list[
    "aws_sdk_bcm_data_exports.types.table_property_description.TablePropertyDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TablePropertyDescriptionList) -> list:
    import aws_sdk_bcm_data_exports.types.table_property_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_data_exports.types.table_property_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TablePropertyDescriptionList:
    import aws_sdk_bcm_data_exports.types.table_property_description

    out: TablePropertyDescriptionList = []
    for item in data:
        out.append(
            aws_sdk_bcm_data_exports.types.table_property_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
