"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InvocationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.citations
    import aws_sdk_iotsitewise.types.string


class InvocationOutput(TypedDict):
    message: NotRequired["aws_sdk_iotsitewise.types.string.String"]
    """<p>The text message of the SiteWise Assistant's response.</p>"""
    citations: NotRequired["aws_sdk_iotsitewise.types.citations.Citations"]
    """<p>A list of citations, and related information for the SiteWise Assistant's response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationOutput) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "citations" in value:
        import aws_sdk_iotsitewise.types.citations

        out["citations"] = aws_sdk_iotsitewise.types.citations.serialize_json(
            value["citations"]
        )
    return out


def deserialize_json(data: dict) -> InvocationOutput:
    out: InvocationOutput = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "citations" in data:
        import aws_sdk_iotsitewise.types.citations

        out["citations"] = aws_sdk_iotsitewise.types.citations.deserialize_json(
            data["citations"]
        )
    return out
