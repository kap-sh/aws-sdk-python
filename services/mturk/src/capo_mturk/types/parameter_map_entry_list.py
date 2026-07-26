"""Generated from Smithy shape ``com.amazonaws.mturk#ParameterMapEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mturk.types.parameter_map_entry

ParameterMapEntryList: TypeAlias = list[
    "capo_mturk.types.parameter_map_entry.ParameterMapEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterMapEntryList) -> list:
    import capo_mturk.types.parameter_map_entry

    out: list = []
    for item in value:
        out.append(capo_mturk.types.parameter_map_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterMapEntryList:
    import capo_mturk.types.parameter_map_entry

    out: ParameterMapEntryList = []
    for item in data:
        out.append(capo_mturk.types.parameter_map_entry.deserialize_aws_json_1_1(item))
    return out
