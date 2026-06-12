"""Generated from Smithy shape ``com.amazonaws.iot#LogTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.log_target_name
    import aws_sdk_iot.types.log_target_type


class LogTarget(TypedDict):
    target_type: "aws_sdk_iot.types.log_target_type.LogTargetType"
    """<p>The target type.</p>"""
    target_name: NotRequired["aws_sdk_iot.types.log_target_name.LogTargetName"]
    """<p>The target name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogTarget) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.log_target_type

    out["targetType"] = aws_sdk_iot.types.log_target_type.serialize_json(
        value["target_type"]
    )
    if "target_name" in value:
        out["targetName"] = value["target_name"]
    return out


def deserialize_json(data: dict) -> LogTarget:
    out: LogTarget = {}  # type: ignore[typeddict-item]
    if "targetType" in data:
        import aws_sdk_iot.types.log_target_type

        out["target_type"] = aws_sdk_iot.types.log_target_type.deserialize_json(
            data["targetType"]
        )
    else:
        raise DeserializationError("LogTarget.target_type required")
    if "targetName" in data:
        out["target_name"] = data["targetName"]
    return out
