"""Generated from Smithy shape ``com.amazonaws.ecr#CvssScoreAdjustmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.cvss_score_adjustment

CvssScoreAdjustmentList: TypeAlias = list[
    "capo_ecr.types.cvss_score_adjustment.CvssScoreAdjustment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CvssScoreAdjustmentList) -> list:
    import capo_ecr.types.cvss_score_adjustment

    out: list = []
    for item in value:
        out.append(capo_ecr.types.cvss_score_adjustment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CvssScoreAdjustmentList:
    import capo_ecr.types.cvss_score_adjustment

    out: CvssScoreAdjustmentList = []
    for item in data:
        out.append(capo_ecr.types.cvss_score_adjustment.deserialize_aws_json_1_1(item))
    return out
