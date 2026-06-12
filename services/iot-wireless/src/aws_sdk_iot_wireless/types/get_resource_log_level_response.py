"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetResourceLogLevelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.log_level


class GetResourceLogLevelResponse(TypedDict):
    log_level: NotRequired["aws_sdk_iot_wireless.types.log_level.LogLevel"]


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceLogLevelResponse) -> dict:
    out: dict = {}
    if "log_level" in value:
        import aws_sdk_iot_wireless.types.log_level

        out["LogLevel"] = aws_sdk_iot_wireless.types.log_level.serialize_json(
            value["log_level"]
        )
    return out


def deserialize_json(data: dict) -> GetResourceLogLevelResponse:
    out: GetResourceLogLevelResponse = {}  # type: ignore[typeddict-item]
    if "LogLevel" in data:
        import aws_sdk_iot_wireless.types.log_level

        out["log_level"] = aws_sdk_iot_wireless.types.log_level.deserialize_json(
            data["LogLevel"]
        )
    return out
