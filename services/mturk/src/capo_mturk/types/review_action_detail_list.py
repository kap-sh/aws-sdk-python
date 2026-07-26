"""Generated from Smithy shape ``com.amazonaws.mturk#ReviewActionDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mturk.types.review_action_detail

ReviewActionDetailList: TypeAlias = list[
    "capo_mturk.types.review_action_detail.ReviewActionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReviewActionDetailList) -> list:
    import capo_mturk.types.review_action_detail

    out: list = []
    for item in value:
        out.append(capo_mturk.types.review_action_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ReviewActionDetailList:
    import capo_mturk.types.review_action_detail

    out: ReviewActionDetailList = []
    for item in data:
        out.append(capo_mturk.types.review_action_detail.deserialize_aws_json_1_1(item))
    return out
