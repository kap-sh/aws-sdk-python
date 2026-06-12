"""Generated from Smithy shape ``com.amazonaws.mturk#ParameterMapEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mturk.types.parameter_map_entry

ParameterMapEntryList: TypeAlias = list[
    "aws_sdk_mturk.types.parameter_map_entry.ParameterMapEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterMapEntryList) -> list:
    import aws_sdk_mturk.types.parameter_map_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_mturk.types.parameter_map_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterMapEntryList:
    import aws_sdk_mturk.types.parameter_map_entry

    out: ParameterMapEntryList = []
    for item in data:
        out.append(
            aws_sdk_mturk.types.parameter_map_entry.deserialize_aws_json_1_1(item)
        )
    return out
