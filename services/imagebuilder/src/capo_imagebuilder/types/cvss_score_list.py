"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CvssScoreList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.cvss_score

CvssScoreList: TypeAlias = list["capo_imagebuilder.types.cvss_score.CvssScore"]


# --- restJson1 ser/de ---
def serialize_json(value: CvssScoreList) -> list:
    import capo_imagebuilder.types.cvss_score

    out: list = []
    for item in value:
        out.append(capo_imagebuilder.types.cvss_score.serialize_json(item))
    return out


def deserialize_json(data: list) -> CvssScoreList:
    import capo_imagebuilder.types.cvss_score

    out: CvssScoreList = []
    for item in data:
        out.append(capo_imagebuilder.types.cvss_score.deserialize_json(item))
    return out
