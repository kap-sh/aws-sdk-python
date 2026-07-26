"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSnippetResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.code_line_list
    import capo_inspector2.types.finding_arn
    import capo_inspector2.types.suggested_fixes


class CodeSnippetResult(TypedDict, closed=True):
    finding_arn: NotRequired["capo_inspector2.types.finding_arn.FindingArn"]
    """<p>The ARN of a finding that the code snippet is associated with.</p>"""
    start_line: NotRequired["int"]
    """<p>The line number of the first line of a code snippet.</p>"""
    end_line: NotRequired["int"]
    """<p>The line number of the last line of a code snippet.</p>"""
    code_snippet: NotRequired["capo_inspector2.types.code_line_list.CodeLineList"]
    """<p>Contains information on the retrieved code snippet.</p>"""
    suggested_fixes: NotRequired["capo_inspector2.types.suggested_fixes.SuggestedFixes"]
    """<p>Details of a suggested code fix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeSnippetResult) -> dict:
    out: dict = {}
    if "finding_arn" in value:
        out["findingArn"] = value["finding_arn"]
    if "start_line" in value:
        out["startLine"] = value["start_line"]
    if "end_line" in value:
        out["endLine"] = value["end_line"]
    if "code_snippet" in value:
        import capo_inspector2.types.code_line_list

        out["codeSnippet"] = capo_inspector2.types.code_line_list.serialize_json(
            value["code_snippet"]
        )
    if "suggested_fixes" in value:
        import capo_inspector2.types.suggested_fixes

        out["suggestedFixes"] = capo_inspector2.types.suggested_fixes.serialize_json(
            value["suggested_fixes"]
        )
    return out


def deserialize_json(data: dict) -> CodeSnippetResult:
    out: CodeSnippetResult = {}  # type: ignore[typeddict-item]
    if "findingArn" in data:
        out["finding_arn"] = data["findingArn"]
    if "startLine" in data:
        out["start_line"] = data["startLine"]
    if "endLine" in data:
        out["end_line"] = data["endLine"]
    if "codeSnippet" in data:
        import capo_inspector2.types.code_line_list

        out["code_snippet"] = capo_inspector2.types.code_line_list.deserialize_json(
            data["codeSnippet"]
        )
    if "suggestedFixes" in data:
        import capo_inspector2.types.suggested_fixes

        out["suggested_fixes"] = capo_inspector2.types.suggested_fixes.deserialize_json(
            data["suggestedFixes"]
        )
    return out
