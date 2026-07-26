"""Generated from Smithy shape ``com.amazonaws.datapipeline#fieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_data_pipeline.types.field

fieldList: TypeAlias = list["capo_data_pipeline.types.field.Field"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: fieldList) -> list:
    import capo_data_pipeline.types.field

    out: list = []
    for item in value:
        out.append(capo_data_pipeline.types.field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> fieldList:
    import capo_data_pipeline.types.field

    out: fieldList = []
    for item in data:
        out.append(capo_data_pipeline.types.field.deserialize_aws_json_1_1(item))
    return out
