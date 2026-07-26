"""Generated from Smithy shape ``com.amazonaws.ivs#GetStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.stream


class GetStreamResponse(TypedDict, closed=True):
    stream: NotRequired["capo_ivs.types.stream.Stream"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamResponse) -> dict:
    out: dict = {}
    if "stream" in value:
        import capo_ivs.types.stream

        out["stream"] = capo_ivs.types.stream.serialize_json(value["stream"])
    return out


def deserialize_json(data: dict) -> GetStreamResponse:
    out: GetStreamResponse = {}  # type: ignore[typeddict-item]
    if "stream" in data:
        import capo_ivs.types.stream

        out["stream"] = capo_ivs.types.stream.deserialize_json(data["stream"])
    return out
