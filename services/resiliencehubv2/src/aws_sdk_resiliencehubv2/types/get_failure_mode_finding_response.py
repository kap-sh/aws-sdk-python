"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetFailureModeFindingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.finding


class GetFailureModeFindingResponse(TypedDict):
    finding: NotRequired["aws_sdk_resiliencehubv2.types.finding.Finding"]
    """<p>The requested finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFailureModeFindingResponse) -> dict:
    out: dict = {}
    if "finding" in value:
        import aws_sdk_resiliencehubv2.types.finding

        out["finding"] = aws_sdk_resiliencehubv2.types.finding.serialize_json(
            value["finding"]
        )
    return out


def deserialize_json(data: dict) -> GetFailureModeFindingResponse:
    out: GetFailureModeFindingResponse = {}  # type: ignore[typeddict-item]
    if "finding" in data:
        import aws_sdk_resiliencehubv2.types.finding

        out["finding"] = aws_sdk_resiliencehubv2.types.finding.deserialize_json(
            data["finding"]
        )
    return out
