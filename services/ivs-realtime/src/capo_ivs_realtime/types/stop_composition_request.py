"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StopCompositionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs_realtime.types.composition_arn


class StopCompositionRequest(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.composition_arn.CompositionArn"
    """<p>ARN of the Composition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopCompositionRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> StopCompositionRequest:
    out: StopCompositionRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("StopCompositionRequest.arn required")
    return out
