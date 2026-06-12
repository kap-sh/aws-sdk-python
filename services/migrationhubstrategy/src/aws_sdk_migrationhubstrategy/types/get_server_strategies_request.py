"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetServerStrategiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.server_id


class GetServerStrategiesRequest(TypedDict):
    server_id: "aws_sdk_migrationhubstrategy.types.server_id.ServerId"
    """<p> The ID of the server. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServerStrategiesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServerStrategiesRequest:
    out: GetServerStrategiesRequest = {}  # type: ignore[typeddict-item]
    return out
