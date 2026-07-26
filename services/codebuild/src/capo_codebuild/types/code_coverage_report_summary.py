"""Generated from Smithy shape ``com.amazonaws.codebuild#CodeCoverageReportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_negative_int
    import capo_codebuild.types.percentage


class CodeCoverageReportSummary(TypedDict, closed=True):
    line_coverage_percentage: NotRequired["capo_codebuild.types.percentage.Percentage"]
    """<p>The percentage of lines that are covered by your tests.</p>"""
    lines_covered: NotRequired["capo_codebuild.types.non_negative_int.NonNegativeInt"]
    """<p>The number of lines that are covered by your tests.</p>"""
    lines_missed: NotRequired["capo_codebuild.types.non_negative_int.NonNegativeInt"]
    """<p>The number of lines that are not covered by your tests.</p>"""
    branch_coverage_percentage: NotRequired[
        "capo_codebuild.types.percentage.Percentage"
    ]
    """<p>The percentage of branches that are covered by your tests.</p>"""
    branches_covered: NotRequired[
        "capo_codebuild.types.non_negative_int.NonNegativeInt"
    ]
    """<p>The number of conditional branches that are covered by your tests.</p>"""
    branches_missed: NotRequired["capo_codebuild.types.non_negative_int.NonNegativeInt"]
    """<p>The number of conditional branches that are not covered by your tests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeCoverageReportSummary) -> dict:
    out: dict = {}
    if "line_coverage_percentage" in value:
        out["lineCoveragePercentage"] = value["line_coverage_percentage"]
    if "lines_covered" in value:
        out["linesCovered"] = value["lines_covered"]
    if "lines_missed" in value:
        out["linesMissed"] = value["lines_missed"]
    if "branch_coverage_percentage" in value:
        out["branchCoveragePercentage"] = value["branch_coverage_percentage"]
    if "branches_covered" in value:
        out["branchesCovered"] = value["branches_covered"]
    if "branches_missed" in value:
        out["branchesMissed"] = value["branches_missed"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeCoverageReportSummary:
    out: CodeCoverageReportSummary = {}  # type: ignore[typeddict-item]
    if "lineCoveragePercentage" in data:
        out["line_coverage_percentage"] = data["lineCoveragePercentage"]
    if "linesCovered" in data:
        out["lines_covered"] = data["linesCovered"]
    if "linesMissed" in data:
        out["lines_missed"] = data["linesMissed"]
    if "branchCoveragePercentage" in data:
        out["branch_coverage_percentage"] = data["branchCoveragePercentage"]
    if "branchesCovered" in data:
        out["branches_covered"] = data["branchesCovered"]
    if "branchesMissed" in data:
        out["branches_missed"] = data["branchesMissed"]
    return out
