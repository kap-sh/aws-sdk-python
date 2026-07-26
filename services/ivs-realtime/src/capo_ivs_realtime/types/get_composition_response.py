"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetCompositionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.composition


class GetCompositionResponse(TypedDict, closed=True):
    composition: NotRequired["capo_ivs_realtime.types.composition.Composition"]
    """<p>The Composition that was returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCompositionResponse) -> dict:
    out: dict = {}
    if "composition" in value:
        import capo_ivs_realtime.types.composition

        out["composition"] = capo_ivs_realtime.types.composition.serialize_json(
            value["composition"]
        )
    return out


def deserialize_json(data: dict) -> GetCompositionResponse:
    out: GetCompositionResponse = {}  # type: ignore[typeddict-item]
    if "composition" in data:
        import capo_ivs_realtime.types.composition

        out["composition"] = capo_ivs_realtime.types.composition.deserialize_json(
            data["composition"]
        )
    return out
