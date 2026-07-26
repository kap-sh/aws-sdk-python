"""Generated from Smithy shape ``com.amazonaws.m2#StartApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.identifier


class StartApplicationRequest(TypedDict, closed=True):
    application_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application you want to start.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartApplicationRequest:
    out: StartApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
