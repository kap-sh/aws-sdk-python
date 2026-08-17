"""Generated from Smithy shape ``com.amazonaws.ecr#CvssScoreList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.cvss_score

CvssScoreList: TypeAlias = list["capo_ecr.types.cvss_score.CvssScore"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CvssScoreList) -> list:
    import capo_ecr.types.cvss_score

    out: list = []
    for item in value:
        out.append(capo_ecr.types.cvss_score.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CvssScoreList:
    import capo_ecr.types.cvss_score

    out: CvssScoreList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecr.types.cvss_score.deserialize_aws_json_1_1(item))
    return out
