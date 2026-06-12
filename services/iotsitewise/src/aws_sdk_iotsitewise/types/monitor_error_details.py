"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MonitorErrorDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.monitor_error_code
    import aws_sdk_iotsitewise.types.monitor_error_message


class MonitorErrorDetails(TypedDict):
    code: NotRequired["aws_sdk_iotsitewise.types.monitor_error_code.MonitorErrorCode"]
    """<p>The error code.</p>"""
    message: NotRequired[
        "aws_sdk_iotsitewise.types.monitor_error_message.MonitorErrorMessage"
    ]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitorErrorDetails) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_iotsitewise.types.monitor_error_code

        out["code"] = aws_sdk_iotsitewise.types.monitor_error_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MonitorErrorDetails:
    out: MonitorErrorDetails = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_iotsitewise.types.monitor_error_code

        out["code"] = aws_sdk_iotsitewise.types.monitor_error_code.deserialize_json(
            data["code"]
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
