"""Generated from Smithy shape ``com.amazonaws.securityagent#LogLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.cloud_watch_log
    import aws_sdk_securityagent.types.log_type


class LogLocation(TypedDict):
    log_type: NotRequired["aws_sdk_securityagent.types.log_type.LogType"]
    """<p>The type of log storage. Currently, only CLOUDWATCH is supported.</p>"""
    cloud_watch_log: NotRequired[
        "aws_sdk_securityagent.types.cloud_watch_log.CloudWatchLog"
    ]
    """<p>The CloudWatch Logs location for the task logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogLocation) -> dict:
    out: dict = {}
    if "log_type" in value:
        import aws_sdk_securityagent.types.log_type

        out["logType"] = aws_sdk_securityagent.types.log_type.serialize_json(
            value["log_type"]
        )
    if "cloud_watch_log" in value:
        import aws_sdk_securityagent.types.cloud_watch_log

        out["cloudWatchLog"] = (
            aws_sdk_securityagent.types.cloud_watch_log.serialize_json(
                value["cloud_watch_log"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogLocation:
    out: LogLocation = {}  # type: ignore[typeddict-item]
    if "logType" in data:
        import aws_sdk_securityagent.types.log_type

        out["log_type"] = aws_sdk_securityagent.types.log_type.deserialize_json(
            data["logType"]
        )
    if "cloudWatchLog" in data:
        import aws_sdk_securityagent.types.cloud_watch_log

        out["cloud_watch_log"] = (
            aws_sdk_securityagent.types.cloud_watch_log.deserialize_json(
                data["cloudWatchLog"]
            )
        )
    return out
