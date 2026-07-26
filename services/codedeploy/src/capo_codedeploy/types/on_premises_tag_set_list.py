"""Generated from Smithy shape ``com.amazonaws.codedeploy#OnPremisesTagSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.tag_filter_list

OnPremisesTagSetList: TypeAlias = list[
    "capo_codedeploy.types.tag_filter_list.TagFilterList"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnPremisesTagSetList) -> list:
    import capo_codedeploy.types.tag_filter_list

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.tag_filter_list.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OnPremisesTagSetList:
    import capo_codedeploy.types.tag_filter_list

    out: OnPremisesTagSetList = []
    for item in data:
        out.append(capo_codedeploy.types.tag_filter_list.deserialize_aws_json_1_1(item))
    return out
