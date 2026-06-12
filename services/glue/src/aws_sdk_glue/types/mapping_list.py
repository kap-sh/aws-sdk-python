"""Generated from Smithy shape ``com.amazonaws.glue#MappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.mapping_entry

MappingList: TypeAlias = list["aws_sdk_glue.types.mapping_entry.MappingEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MappingList) -> list:
    import aws_sdk_glue.types.mapping_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.mapping_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MappingList:
    import aws_sdk_glue.types.mapping_entry

    out: MappingList = []
    for item in data:
        out.append(aws_sdk_glue.types.mapping_entry.deserialize_aws_json_1_1(item))
    return out
