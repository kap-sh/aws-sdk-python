"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetResourceLogLevelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.log_level


class GetResourceLogLevelResponse(TypedDict, closed=True):
    log_level: NotRequired["capo_iot_wireless.types.log_level.LogLevel"]


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceLogLevelResponse) -> dict:
    out: dict = {}
    if "log_level" in value:
        import capo_iot_wireless.types.log_level

        out["LogLevel"] = capo_iot_wireless.types.log_level.serialize_json(
            value["log_level"]
        )
    return out


def deserialize_json(data: dict) -> GetResourceLogLevelResponse:
    out: GetResourceLogLevelResponse = {}  # type: ignore[typeddict-item]
    if "LogLevel" in data:
        import capo_iot_wireless.types.log_level

        out["log_level"] = capo_iot_wireless.types.log_level.deserialize_json(
            data["LogLevel"]
        )
    return out
