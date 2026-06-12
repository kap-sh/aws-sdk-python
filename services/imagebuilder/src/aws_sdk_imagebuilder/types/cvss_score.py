"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CvssScore``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.non_negative_double


class CvssScore(TypedDict):
    base_score: NotRequired[
        "aws_sdk_imagebuilder.types.non_negative_double.NonNegativeDouble"
    ]
    """<p>The CVSS base score.</p>"""
    scoring_vector: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The vector string of the CVSS score.</p>"""
    version: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The CVSS version that generated the score.</p>"""
    source: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The source of the CVSS score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CvssScore) -> dict:
    out: dict = {}
    if "base_score" in value:
        out["baseScore"] = value["base_score"]
    if "scoring_vector" in value:
        out["scoringVector"] = value["scoring_vector"]
    if "version" in value:
        out["version"] = value["version"]
    if "source" in value:
        out["source"] = value["source"]
    return out


def deserialize_json(data: dict) -> CvssScore:
    out: CvssScore = {}  # type: ignore[typeddict-item]
    if "baseScore" in data:
        out["base_score"] = data["baseScore"]
    if "scoringVector" in data:
        out["scoring_vector"] = data["scoringVector"]
    if "version" in data:
        out["version"] = data["version"]
    if "source" in data:
        out["source"] = data["source"]
    return out
