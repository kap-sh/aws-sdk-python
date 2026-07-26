"""Generated from Smithy shape ``com.amazonaws.macie2#GetFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_finding


class GetFindingsResponse(TypedDict, closed=True):
    findings: NotRequired["capo_macie2.types.__list_of_finding.__listOfFinding"]
    """<p>An array of objects, one for each finding that matches the criteria specified in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsResponse) -> dict:
    out: dict = {}
    if "findings" in value:
        import capo_macie2.types.__list_of_finding

        out["findings"] = capo_macie2.types.__list_of_finding.serialize_json(
            value["findings"]
        )
    return out


def deserialize_json(data: dict) -> GetFindingsResponse:
    out: GetFindingsResponse = {}  # type: ignore[typeddict-item]
    if "findings" in data:
        import capo_macie2.types.__list_of_finding

        out["findings"] = capo_macie2.types.__list_of_finding.deserialize_json(
            data["findings"]
        )
    return out
