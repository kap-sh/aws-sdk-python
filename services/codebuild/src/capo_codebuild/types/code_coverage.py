"""Generated from Smithy shape ``com.amazonaws.codebuild#CodeCoverage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.non_negative_int
    import capo_codebuild.types.percentage
    import capo_codebuild.types.timestamp


class CodeCoverage(TypedDict, closed=True):
    id: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the code coverage report.</p>"""
    report_arn: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the report.</p>"""
    file_path: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The path of the test report file.</p>"""
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
    expired: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>The date and time that the tests were run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeCoverage) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "report_arn" in value:
        out["reportARN"] = value["report_arn"]
    if "file_path" in value:
        out["filePath"] = value["file_path"]
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
    if "expired" in value:
        import capo_codebuild.types.timestamp

        out["expired"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["expired"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeCoverage:
    out: CodeCoverage = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "reportARN" in data:
        out["report_arn"] = data["reportARN"]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
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
    if "expired" in data:
        import capo_codebuild.types.timestamp

        out["expired"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["expired"]
        )
    return out
