"""Generated from Smithy shape ``com.amazonaws.m2#GetEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.identifier


class GetEnvironmentRequest(TypedDict, closed=True):
    environment_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the runtime environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEnvironmentRequest:
    out: GetEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
