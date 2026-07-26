"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateFailureModeFindingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.finding


class UpdateFailureModeFindingResponse(TypedDict, closed=True):
    finding: NotRequired["capo_resiliencehubv2.types.finding.Finding"]
    """<p>The updated finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFailureModeFindingResponse) -> dict:
    out: dict = {}
    if "finding" in value:
        import capo_resiliencehubv2.types.finding

        out["finding"] = capo_resiliencehubv2.types.finding.serialize_json(
            value["finding"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFailureModeFindingResponse:
    out: UpdateFailureModeFindingResponse = {}  # type: ignore[typeddict-item]
    if "finding" in data:
        import capo_resiliencehubv2.types.finding

        out["finding"] = capo_resiliencehubv2.types.finding.deserialize_json(
            data["finding"]
        )
    return out
