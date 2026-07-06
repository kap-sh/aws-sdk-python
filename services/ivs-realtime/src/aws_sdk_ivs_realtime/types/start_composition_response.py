"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StartCompositionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.composition


class StartCompositionResponse(TypedDict, closed=True):
    composition: NotRequired["aws_sdk_ivs_realtime.types.composition.Composition"]
    """<p>The Composition that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCompositionResponse) -> dict:
    out: dict = {}
    if "composition" in value:
        import aws_sdk_ivs_realtime.types.composition

        out["composition"] = aws_sdk_ivs_realtime.types.composition.serialize_json(
            value["composition"]
        )
    return out


def deserialize_json(data: dict) -> StartCompositionResponse:
    out: StartCompositionResponse = {}  # type: ignore[typeddict-item]
    if "composition" in data:
        import aws_sdk_ivs_realtime.types.composition

        out["composition"] = aws_sdk_ivs_realtime.types.composition.deserialize_json(
            data["composition"]
        )
    return out
