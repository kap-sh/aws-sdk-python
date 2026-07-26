"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetFindingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.finding


class GetFindingResponse(TypedDict, closed=True):
    finding: NotRequired["capo_accessanalyzer.types.finding.Finding"]
    """<p>A <code>finding</code> object that contains finding details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingResponse) -> dict:
    out: dict = {}
    if "finding" in value:
        import capo_accessanalyzer.types.finding

        out["finding"] = capo_accessanalyzer.types.finding.serialize_json(
            value["finding"]
        )
    return out


def deserialize_json(data: dict) -> GetFindingResponse:
    out: GetFindingResponse = {}  # type: ignore[typeddict-item]
    if "finding" in data:
        import capo_accessanalyzer.types.finding

        out["finding"] = capo_accessanalyzer.types.finding.deserialize_json(
            data["finding"]
        )
    return out
