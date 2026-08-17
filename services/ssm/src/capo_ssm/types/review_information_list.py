"""Generated from Smithy shape ``com.amazonaws.ssm#ReviewInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.review_information

ReviewInformationList: TypeAlias = list[
    "capo_ssm.types.review_information.ReviewInformation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReviewInformationList) -> list:
    import capo_ssm.types.review_information

    out: list = []
    for item in value:
        out.append(capo_ssm.types.review_information.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ReviewInformationList:
    import capo_ssm.types.review_information

    out: ReviewInformationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.review_information.deserialize_aws_json_1_1(item))
    return out
