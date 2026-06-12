"""Generated from Smithy shape ``com.amazonaws.glue#OptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.option

OptionList: TypeAlias = list["aws_sdk_glue.types.option.Option"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptionList) -> list:
    import aws_sdk_glue.types.option

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.option.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OptionList:
    import aws_sdk_glue.types.option

    out: OptionList = []
    for item in data:
        out.append(aws_sdk_glue.types.option.deserialize_aws_json_1_1(item))
    return out
