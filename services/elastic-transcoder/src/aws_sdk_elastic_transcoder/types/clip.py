"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Clip``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.time_span


class Clip(TypedDict):
    time_span: NotRequired["aws_sdk_elastic_transcoder.types.time_span.TimeSpan"]
    """<p>Settings that determine when a clip begins and how long it lasts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Clip) -> dict:
    out: dict = {}
    if "time_span" in value:
        import aws_sdk_elastic_transcoder.types.time_span

        out["TimeSpan"] = aws_sdk_elastic_transcoder.types.time_span.serialize_json(
            value["time_span"]
        )
    return out


def deserialize_json(data: dict) -> Clip:
    out: Clip = {}  # type: ignore[typeddict-item]
    if "TimeSpan" in data:
        import aws_sdk_elastic_transcoder.types.time_span

        out["time_span"] = aws_sdk_elastic_transcoder.types.time_span.deserialize_json(
            data["TimeSpan"]
        )
    return out
