"""Generated from Smithy shape ``com.amazonaws.connect#ContactAnalysis``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.transcript


class ContactAnalysis(TypedDict):
    transcript: NotRequired["aws_sdk_connect.types.transcript.Transcript"]
    """<p>Search criteria based on transcript analyzed by Connect Customer Contact Lens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactAnalysis) -> dict:
    out: dict = {}
    if "transcript" in value:
        import aws_sdk_connect.types.transcript

        out["Transcript"] = aws_sdk_connect.types.transcript.serialize_json(
            value["transcript"]
        )
    return out


def deserialize_json(data: dict) -> ContactAnalysis:
    out: ContactAnalysis = {}  # type: ignore[typeddict-item]
    if "Transcript" in data:
        import aws_sdk_connect.types.transcript

        out["transcript"] = aws_sdk_connect.types.transcript.deserialize_json(
            data["Transcript"]
        )
    return out
