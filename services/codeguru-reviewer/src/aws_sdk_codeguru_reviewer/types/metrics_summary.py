"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#MetricsSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.findings_count
    import aws_sdk_codeguru_reviewer.types.lines_of_code_count


class MetricsSummary(TypedDict):
    metered_lines_of_code_count: NotRequired[
        "aws_sdk_codeguru_reviewer.types.lines_of_code_count.LinesOfCodeCount"
    ]
    """<p>Lines of code metered in the code review. For the initial code review pull request and all subsequent revisions, this includes all lines of code in the files added to the pull request. In subsequent revisions, for files that already existed in the pull request, this includes only the changed lines of code. In both cases, this does not include non-code lines such as comments and import statements. For example, if you submit a pull request containing 5 files, each with 500 lines of code, and in a subsequent revision you added a new file with 200 lines of code, and also modified a total of 25 lines across the initial 5 files, <code>MeteredLinesOfCodeCount</code> includes the first 5 files (5 * 500 = 2,500 lines), the new file (200 lines) and the 25 changed lines of code for a total of 2,725 lines of code.</p>"""
    suppressed_lines_of_code_count: NotRequired[
        "aws_sdk_codeguru_reviewer.types.lines_of_code_count.LinesOfCodeCount"
    ]
    """<p>Lines of code suppressed in the code review based on the <code>excludeFiles</code> element in the <code>aws-codeguru-reviewer.yml</code> file. For full repository analyses, this number includes all lines of code in the files that are suppressed. For pull requests, this number only includes the <i>changed</i> lines of code that are suppressed. In both cases, this number does not include non-code lines such as comments and import statements. For example, if you initiate a full repository analysis on a repository containing 5 files, each file with 100 lines of code, and 2 files are listed as excluded in the <code>aws-codeguru-reviewer.yml</code> file, then <code>SuppressedLinesOfCodeCount</code> returns 200 (2 * 100) as the total number of lines of code suppressed. However, if you submit a pull request for the same repository, then <code>SuppressedLinesOfCodeCount</code> only includes the lines in the 2 files that changed. If only 1 of the 2 files changed in the pull request, then <code>SuppressedLinesOfCodeCount</code> returns 100 (1 * 100) as the total number of lines of code suppressed.</p>"""
    findings_count: NotRequired[
        "aws_sdk_codeguru_reviewer.types.findings_count.FindingsCount"
    ]
    """<p>Total number of recommendations found in the code review.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricsSummary) -> dict:
    out: dict = {}
    if "metered_lines_of_code_count" in value:
        out["MeteredLinesOfCodeCount"] = value["metered_lines_of_code_count"]
    if "suppressed_lines_of_code_count" in value:
        out["SuppressedLinesOfCodeCount"] = value["suppressed_lines_of_code_count"]
    if "findings_count" in value:
        out["FindingsCount"] = value["findings_count"]
    return out


def deserialize_json(data: dict) -> MetricsSummary:
    out: MetricsSummary = {}  # type: ignore[typeddict-item]
    if "MeteredLinesOfCodeCount" in data:
        out["metered_lines_of_code_count"] = data["MeteredLinesOfCodeCount"]
    if "SuppressedLinesOfCodeCount" in data:
        out["suppressed_lines_of_code_count"] = data["SuppressedLinesOfCodeCount"]
    if "FindingsCount" in data:
        out["findings_count"] = data["FindingsCount"]
    return out
