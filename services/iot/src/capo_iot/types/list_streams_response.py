"""Generated from Smithy shape ``com.amazonaws.iot#ListStreamsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.streams_summary


class ListStreamsResponse(TypedDict, closed=True):
    streams: NotRequired["capo_iot.types.streams_summary.StreamsSummary"]
    """<p>A list of streams.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>A token used to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamsResponse) -> dict:
    out: dict = {}
    if "streams" in value:
        import capo_iot.types.streams_summary

        out["streams"] = capo_iot.types.streams_summary.serialize_json(value["streams"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStreamsResponse:
    out: ListStreamsResponse = {}  # type: ignore[typeddict-item]
    if "streams" in data:
        import capo_iot.types.streams_summary

        out["streams"] = capo_iot.types.streams_summary.deserialize_json(
            data["streams"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
