"""Generated from Smithy shape ``com.amazonaws.datapipeline#tagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_data_pipeline.types.tag

tagList: TypeAlias = list["capo_data_pipeline.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: tagList) -> list:
    import capo_data_pipeline.types.tag

    out: list = []
    for item in value:
        out.append(capo_data_pipeline.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> tagList:
    import capo_data_pipeline.types.tag

    out: tagList = []
    for item in data:
        out.append(capo_data_pipeline.types.tag.deserialize_aws_json_1_1(item))
    return out
