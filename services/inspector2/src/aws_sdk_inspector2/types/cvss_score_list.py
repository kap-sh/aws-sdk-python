"""Generated from Smithy shape ``com.amazonaws.inspector2#CvssScoreList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cvss_score

CvssScoreList: TypeAlias = list["aws_sdk_inspector2.types.cvss_score.CvssScore"]


# --- restJson1 ser/de ---
def serialize_json(value: CvssScoreList) -> list:
    import aws_sdk_inspector2.types.cvss_score

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.cvss_score.serialize_json(item))
    return out


def deserialize_json(data: list) -> CvssScoreList:
    import aws_sdk_inspector2.types.cvss_score

    out: CvssScoreList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.cvss_score.deserialize_json(item))
    return out
