"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.flow


class CreateFlowResponse(TypedDict, closed=True):
    flow: NotRequired["capo_mediaconnect.types.flow.Flow"]
    """<p> The flow that you created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFlowResponse) -> dict:
    out: dict = {}
    if "flow" in value:
        import capo_mediaconnect.types.flow

        out["flow"] = capo_mediaconnect.types.flow.serialize_json(value["flow"])
    return out


def deserialize_json(data: dict) -> CreateFlowResponse:
    out: CreateFlowResponse = {}  # type: ignore[typeddict-item]
    if "flow" in data:
        import capo_mediaconnect.types.flow

        out["flow"] = capo_mediaconnect.types.flow.deserialize_json(data["flow"])
    return out
