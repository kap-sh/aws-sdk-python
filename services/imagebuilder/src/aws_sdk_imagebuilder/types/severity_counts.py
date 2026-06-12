"""Generated from Smithy shape ``com.amazonaws.imagebuilder#SeverityCounts``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.severity_count_number


class SeverityCounts(TypedDict):
    all: NotRequired[
        "aws_sdk_imagebuilder.types.severity_count_number.SeverityCountNumber"
    ]
    """<p>The total number of findings across all severity levels for the specified filter.</p>"""
    critical: NotRequired[
        "aws_sdk_imagebuilder.types.severity_count_number.SeverityCountNumber"
    ]
    """<p>The number of critical severity findings for the specified filter.</p>"""
    high: NotRequired[
        "aws_sdk_imagebuilder.types.severity_count_number.SeverityCountNumber"
    ]
    """<p>The number of high severity findings for the specified filter.</p>"""
    medium: NotRequired[
        "aws_sdk_imagebuilder.types.severity_count_number.SeverityCountNumber"
    ]
    """<p>The number of medium severity findings for the specified filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SeverityCounts) -> dict:
    out: dict = {}
    if "all" in value:
        out["all"] = value["all"]
    if "critical" in value:
        out["critical"] = value["critical"]
    if "high" in value:
        out["high"] = value["high"]
    if "medium" in value:
        out["medium"] = value["medium"]
    return out


def deserialize_json(data: dict) -> SeverityCounts:
    out: SeverityCounts = {}  # type: ignore[typeddict-item]
    if "all" in data:
        out["all"] = data["all"]
    if "critical" in data:
        out["critical"] = data["critical"]
    if "high" in data:
        out["high"] = data["high"]
    if "medium" in data:
        out["medium"] = data["medium"]
    return out
