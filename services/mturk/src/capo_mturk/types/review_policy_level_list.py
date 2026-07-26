"""Generated from Smithy shape ``com.amazonaws.mturk#ReviewPolicyLevelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mturk.types.review_policy_level

ReviewPolicyLevelList: TypeAlias = list[
    "capo_mturk.types.review_policy_level.ReviewPolicyLevel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReviewPolicyLevelList) -> list:
    import capo_mturk.types.review_policy_level

    out: list = []
    for item in value:
        out.append(capo_mturk.types.review_policy_level.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ReviewPolicyLevelList:
    import capo_mturk.types.review_policy_level

    out: ReviewPolicyLevelList = []
    for item in data:
        out.append(capo_mturk.types.review_policy_level.deserialize_aws_json_1_1(item))
    return out
