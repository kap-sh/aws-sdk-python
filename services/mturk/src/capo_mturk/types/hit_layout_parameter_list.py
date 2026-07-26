"""Generated from Smithy shape ``com.amazonaws.mturk#HITLayoutParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mturk.types.hit_layout_parameter

HITLayoutParameterList: TypeAlias = list[
    "capo_mturk.types.hit_layout_parameter.HITLayoutParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HITLayoutParameterList) -> list:
    import capo_mturk.types.hit_layout_parameter

    out: list = []
    for item in value:
        out.append(capo_mturk.types.hit_layout_parameter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> HITLayoutParameterList:
    import capo_mturk.types.hit_layout_parameter

    out: HITLayoutParameterList = []
    for item in data:
        out.append(capo_mturk.types.hit_layout_parameter.deserialize_aws_json_1_1(item))
    return out
