"""Generated from Smithy shape ``com.amazonaws.mturk#ReviewResultDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mturk.types.review_result_detail

ReviewResultDetailList: TypeAlias = list[
    "aws_sdk_mturk.types.review_result_detail.ReviewResultDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReviewResultDetailList) -> list:
    import aws_sdk_mturk.types.review_result_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mturk.types.review_result_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReviewResultDetailList:
    import aws_sdk_mturk.types.review_result_detail

    out: ReviewResultDetailList = []
    for item in data:
        out.append(
            aws_sdk_mturk.types.review_result_detail.deserialize_aws_json_1_1(item)
        )
    return out
