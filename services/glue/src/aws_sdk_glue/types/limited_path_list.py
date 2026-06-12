"""Generated from Smithy shape ``com.amazonaws.glue#LimitedPathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.limited_string_list

LimitedPathList: TypeAlias = list[
    "aws_sdk_glue.types.limited_string_list.LimitedStringList"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LimitedPathList) -> list:
    import aws_sdk_glue.types.limited_string_list

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.limited_string_list.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LimitedPathList:
    import aws_sdk_glue.types.limited_string_list

    out: LimitedPathList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.limited_string_list.deserialize_aws_json_1_1(item)
        )
    return out
