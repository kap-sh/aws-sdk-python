"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ReasonSummary``."""

from typing_extensions import NotRequired, TypedDict


class ReasonSummary(TypedDict, closed=True):
    description: NotRequired["str"]
    """<p>A description of the reasoning of a result of checking for access.</p>"""
    statement_index: NotRequired["int"]
    """<p>The index number of the reason statement.</p>"""
    statement_id: NotRequired["str"]
    """<p>The identifier for the reason statement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReasonSummary) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "statement_index" in value:
        out["statementIndex"] = value["statement_index"]
    if "statement_id" in value:
        out["statementId"] = value["statement_id"]
    return out


def deserialize_json(data: dict) -> ReasonSummary:
    out: ReasonSummary = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "statementIndex" in data:
        out["statement_index"] = data["statementIndex"]
    if "statementId" in data:
        out["statement_id"] = data["statementId"]
    return out
