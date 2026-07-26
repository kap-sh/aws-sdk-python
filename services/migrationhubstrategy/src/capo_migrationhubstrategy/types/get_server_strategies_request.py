"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetServerStrategiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.server_id


class GetServerStrategiesRequest(TypedDict, closed=True):
    server_id: "capo_migrationhubstrategy.types.server_id.ServerId"
    """<p> The ID of the server. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServerStrategiesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServerStrategiesRequest:
    out: GetServerStrategiesRequest = {}  # type: ignore[typeddict-item]
    return out
