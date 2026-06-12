"""Generated from Smithy shape ``com.amazonaws.datapipeline#SelectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.selector

SelectorList: TypeAlias = list["aws_sdk_data_pipeline.types.selector.Selector"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectorList) -> list:
    import aws_sdk_data_pipeline.types.selector

    out: list = []
    for item in value:
        out.append(aws_sdk_data_pipeline.types.selector.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SelectorList:
    import aws_sdk_data_pipeline.types.selector

    out: SelectorList = []
    for item in data:
        out.append(aws_sdk_data_pipeline.types.selector.deserialize_aws_json_1_1(item))
    return out
