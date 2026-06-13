"""Generated from Smithy shape ``com.amazonaws.inspector2#CvssScoreAdjustmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cvss_score_adjustment

CvssScoreAdjustmentList: TypeAlias = list[
    "aws_sdk_inspector2.types.cvss_score_adjustment.CvssScoreAdjustment"
]


# --- restJson1 ser/de ---
def serialize_json(value: CvssScoreAdjustmentList) -> list:
    import aws_sdk_inspector2.types.cvss_score_adjustment

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.cvss_score_adjustment.serialize_json(item))
    return out


def deserialize_json(data: list) -> CvssScoreAdjustmentList:
    import aws_sdk_inspector2.types.cvss_score_adjustment

    out: CvssScoreAdjustmentList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.cvss_score_adjustment.deserialize_json(item)
        )
    return out
