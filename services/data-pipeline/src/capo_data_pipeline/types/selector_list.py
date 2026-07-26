"""Generated from Smithy shape ``com.amazonaws.datapipeline#SelectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_data_pipeline.types.selector

SelectorList: TypeAlias = list["capo_data_pipeline.types.selector.Selector"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectorList) -> list:
    import capo_data_pipeline.types.selector

    out: list = []
    for item in value:
        out.append(capo_data_pipeline.types.selector.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SelectorList:
    import capo_data_pipeline.types.selector

    out: SelectorList = []
    for item in data:
        out.append(capo_data_pipeline.types.selector.deserialize_aws_json_1_1(item))
    return out
