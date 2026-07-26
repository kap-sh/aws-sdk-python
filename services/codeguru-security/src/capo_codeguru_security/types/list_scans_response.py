"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ListScansResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_security.types.next_token
    import capo_codeguru_security.types.scan_summaries


class ListScansResponse(TypedDict, closed=True):
    summaries: NotRequired["capo_codeguru_security.types.scan_summaries.ScanSummaries"]
    """<p>A list of <code>ScanSummary</code> objects with information about all scans in an account.</p>"""
    next_token: NotRequired["capo_codeguru_security.types.next_token.NextToken"]
    """<p>A pagination token. You can use this in future calls to <code>ListScans</code> to continue listing results after the current page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScansResponse) -> dict:
    out: dict = {}
    if "summaries" in value:
        import capo_codeguru_security.types.scan_summaries

        out["summaries"] = capo_codeguru_security.types.scan_summaries.serialize_json(
            value["summaries"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListScansResponse:
    out: ListScansResponse = {}  # type: ignore[typeddict-item]
    if "summaries" in data:
        import capo_codeguru_security.types.scan_summaries

        out["summaries"] = capo_codeguru_security.types.scan_summaries.deserialize_json(
            data["summaries"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
