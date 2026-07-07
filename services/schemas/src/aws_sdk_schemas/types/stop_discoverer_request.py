"""Generated from Smithy shape ``com.amazonaws.schemas#StopDiscovererRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string


class StopDiscovererRequest(TypedDict, closed=True):
    discoverer_id: "aws_sdk_schemas.types.__string.__string"
    """<p>The ID of the discoverer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopDiscovererRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopDiscovererRequest:
    out: StopDiscovererRequest = {}  # type: ignore[typeddict-item]
    return out
