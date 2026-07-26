"""Generated from Smithy shape ``com.amazonaws.glue#OptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.option

OptionList: TypeAlias = list["capo_glue.types.option.Option"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptionList) -> list:
    import capo_glue.types.option

    out: list = []
    for item in value:
        out.append(capo_glue.types.option.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OptionList:
    import capo_glue.types.option

    out: OptionList = []
    for item in data:
        out.append(capo_glue.types.option.deserialize_aws_json_1_1(item))
    return out
