"""Generated from Smithy shape ``com.amazonaws.mturk#HITLayoutParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mturk.types.hit_layout_parameter

HITLayoutParameterList: TypeAlias = list[
    "aws_sdk_mturk.types.hit_layout_parameter.HITLayoutParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HITLayoutParameterList) -> list:
    import aws_sdk_mturk.types.hit_layout_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mturk.types.hit_layout_parameter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HITLayoutParameterList:
    import aws_sdk_mturk.types.hit_layout_parameter

    out: HITLayoutParameterList = []
    for item in data:
        out.append(
            aws_sdk_mturk.types.hit_layout_parameter.deserialize_aws_json_1_1(item)
        )
    return out
