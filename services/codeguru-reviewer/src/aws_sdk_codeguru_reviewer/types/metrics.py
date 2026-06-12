"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#Metrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.findings_count
    import aws_sdk_codeguru_reviewer.types.lines_of_code_count


class Metrics(TypedDict):
    metered_lines_of_code_count: NotRequired[
        "aws_sdk_codeguru_reviewer.types.lines_of_code_count.LinesOfCodeCount"
    ]
    """<p> <code>MeteredLinesOfCodeCount</code> is the number of lines of code in the repository where the code review happened. This does not include non-code lines such as comments and blank lines.</p>"""
    suppressed_lines_of_code_count: NotRequired[
        "aws_sdk_codeguru_reviewer.types.lines_of_code_count.LinesOfCodeCount"
    ]
    """<p> <code>SuppressedLinesOfCodeCount</code> is the number of lines of code in the repository where the code review happened that CodeGuru Reviewer did not analyze. The lines suppressed in the analysis is based on the <code>excludeFiles</code> variable in the <code>aws-codeguru-reviewer.yml</code> file. This number does not include non-code lines such as comments and blank lines. </p>"""
    findings_count: NotRequired[
        "aws_sdk_codeguru_reviewer.types.findings_count.FindingsCount"
    ]
    """<p>Total number of recommendations found in the code review.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Metrics) -> dict:
    out: dict = {}
    if "metered_lines_of_code_count" in value:
        out["MeteredLinesOfCodeCount"] = value["metered_lines_of_code_count"]
    if "suppressed_lines_of_code_count" in value:
        out["SuppressedLinesOfCodeCount"] = value["suppressed_lines_of_code_count"]
    if "findings_count" in value:
        out["FindingsCount"] = value["findings_count"]
    return out


def deserialize_json(data: dict) -> Metrics:
    out: Metrics = {}  # type: ignore[typeddict-item]
    if "MeteredLinesOfCodeCount" in data:
        out["metered_lines_of_code_count"] = data["MeteredLinesOfCodeCount"]
    if "SuppressedLinesOfCodeCount" in data:
        out["suppressed_lines_of_code_count"] = data["SuppressedLinesOfCodeCount"]
    if "FindingsCount" in data:
        out["findings_count"] = data["FindingsCount"]
    return out
