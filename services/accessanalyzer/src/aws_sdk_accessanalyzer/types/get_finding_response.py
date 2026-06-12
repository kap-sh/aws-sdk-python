"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetFindingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.finding


class GetFindingResponse(TypedDict):
    finding: NotRequired["aws_sdk_accessanalyzer.types.finding.Finding"]
    """<p>A <code>finding</code> object that contains finding details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingResponse) -> dict:
    out: dict = {}
    if "finding" in value:
        import aws_sdk_accessanalyzer.types.finding

        out["finding"] = aws_sdk_accessanalyzer.types.finding.serialize_json(
            value["finding"]
        )
    return out


def deserialize_json(data: dict) -> GetFindingResponse:
    out: GetFindingResponse = {}  # type: ignore[typeddict-item]
    if "finding" in data:
        import aws_sdk_accessanalyzer.types.finding

        out["finding"] = aws_sdk_accessanalyzer.types.finding.deserialize_json(
            data["finding"]
        )
    return out
