"""Generated from Smithy shape ``com.amazonaws.swf#ActivityTypeInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_swf.types.activity_type_info

ActivityTypeInfoList: TypeAlias = list[
    "capo_swf.types.activity_type_info.ActivityTypeInfo"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityTypeInfoList) -> list:
    import capo_swf.types.activity_type_info

    out: list = []
    for item in value:
        out.append(capo_swf.types.activity_type_info.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ActivityTypeInfoList:
    import capo_swf.types.activity_type_info

    out: ActivityTypeInfoList = []
    for item in data:
        out.append(capo_swf.types.activity_type_info.deserialize_aws_json_1_0(item))
    return out
