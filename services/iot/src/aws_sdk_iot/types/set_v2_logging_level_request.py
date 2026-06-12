"""Generated from Smithy shape ``com.amazonaws.iot#SetV2LoggingLevelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.log_level
    import aws_sdk_iot.types.log_target


class SetV2LoggingLevelRequest(TypedDict):
    log_target: "aws_sdk_iot.types.log_target.LogTarget"
    """<p>The log target.</p>"""
    log_level: "aws_sdk_iot.types.log_level.LogLevel"
    """<p>The log level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetV2LoggingLevelRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.log_target

    out["logTarget"] = aws_sdk_iot.types.log_target.serialize_json(value["log_target"])
    import aws_sdk_iot.types.log_level

    out["logLevel"] = aws_sdk_iot.types.log_level.serialize_json(value["log_level"])
    return out


def deserialize_json(data: dict) -> SetV2LoggingLevelRequest:
    out: SetV2LoggingLevelRequest = {}  # type: ignore[typeddict-item]
    if "logTarget" in data:
        import aws_sdk_iot.types.log_target

        out["log_target"] = aws_sdk_iot.types.log_target.deserialize_json(
            data["logTarget"]
        )
    else:
        raise DeserializationError("SetV2LoggingLevelRequest.log_target required")
    if "logLevel" in data:
        import aws_sdk_iot.types.log_level

        out["log_level"] = aws_sdk_iot.types.log_level.deserialize_json(
            data["logLevel"]
        )
    else:
        raise DeserializationError("SetV2LoggingLevelRequest.log_level required")
    return out
