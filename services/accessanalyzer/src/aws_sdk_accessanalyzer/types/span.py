"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#Span``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.position


class Span(TypedDict, closed=True):
    start: "aws_sdk_accessanalyzer.types.position.Position"
    """<p>The start position of the span (inclusive).</p>"""
    end: "aws_sdk_accessanalyzer.types.position.Position"
    """<p>The end position of the span (exclusive).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Span) -> dict:
    out: dict = {}
    import aws_sdk_accessanalyzer.types.position

    out["start"] = aws_sdk_accessanalyzer.types.position.serialize_json(value["start"])
    import aws_sdk_accessanalyzer.types.position

    out["end"] = aws_sdk_accessanalyzer.types.position.serialize_json(value["end"])
    return out


def deserialize_json(data: dict) -> Span:
    out: Span = {}  # type: ignore[typeddict-item]
    if "start" in data:
        import aws_sdk_accessanalyzer.types.position

        out["start"] = aws_sdk_accessanalyzer.types.position.deserialize_json(
            data["start"]
        )
    else:
        raise DeserializationError("Span.start required")
    if "end" in data:
        import aws_sdk_accessanalyzer.types.position

        out["end"] = aws_sdk_accessanalyzer.types.position.deserialize_json(data["end"])
    else:
        raise DeserializationError("Span.end required")
    return out
