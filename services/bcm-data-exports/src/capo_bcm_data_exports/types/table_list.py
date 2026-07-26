"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#TableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.table

TableList: TypeAlias = list["capo_bcm_data_exports.types.table.Table"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableList) -> list:
    import capo_bcm_data_exports.types.table

    out: list = []
    for item in value:
        out.append(capo_bcm_data_exports.types.table.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TableList:
    import capo_bcm_data_exports.types.table

    out: TableList = []
    for item in data:
        out.append(capo_bcm_data_exports.types.table.deserialize_aws_json_1_1(item))
    return out
