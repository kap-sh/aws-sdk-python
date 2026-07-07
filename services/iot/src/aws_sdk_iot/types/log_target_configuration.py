"""Generated from Smithy shape ``com.amazonaws.iot#LogTargetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.log_level
    import aws_sdk_iot.types.log_target


class LogTargetConfiguration(TypedDict, closed=True):
    log_target: NotRequired["aws_sdk_iot.types.log_target.LogTarget"]
    """<p>A log target</p>"""
    log_level: NotRequired["aws_sdk_iot.types.log_level.LogLevel"]
    """<p>The logging level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogTargetConfiguration) -> dict:
    out: dict = {}
    if "log_target" in value:
        import aws_sdk_iot.types.log_target

        out["logTarget"] = aws_sdk_iot.types.log_target.serialize_json(
            value["log_target"]
        )
    if "log_level" in value:
        import aws_sdk_iot.types.log_level

        out["logLevel"] = aws_sdk_iot.types.log_level.serialize_json(value["log_level"])
    return out


def deserialize_json(data: dict) -> LogTargetConfiguration:
    out: LogTargetConfiguration = {}  # type: ignore[typeddict-item]
    if "logTarget" in data:
        import aws_sdk_iot.types.log_target

        out["log_target"] = aws_sdk_iot.types.log_target.deserialize_json(
            data["logTarget"]
        )
    if "logLevel" in data:
        import aws_sdk_iot.types.log_level

        out["log_level"] = aws_sdk_iot.types.log_level.deserialize_json(
            data["logLevel"]
        )
    return out
