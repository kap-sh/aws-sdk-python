"""Generated from Smithy shape ``com.amazonaws.securityagent#LogLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.cloud_watch_log
    import capo_securityagent.types.log_type


class LogLocation(TypedDict, closed=True):
    log_type: NotRequired["capo_securityagent.types.log_type.LogType"]
    """<p>The type of log storage. Currently, only CLOUDWATCH is supported.</p>"""
    cloud_watch_log: NotRequired[
        "capo_securityagent.types.cloud_watch_log.CloudWatchLog"
    ]
    """<p>The CloudWatch Logs location for the task logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogLocation) -> dict:
    out: dict = {}
    if "log_type" in value:
        import capo_securityagent.types.log_type

        out["logType"] = capo_securityagent.types.log_type.serialize_json(
            value["log_type"]
        )
    if "cloud_watch_log" in value:
        import capo_securityagent.types.cloud_watch_log

        out["cloudWatchLog"] = capo_securityagent.types.cloud_watch_log.serialize_json(
            value["cloud_watch_log"]
        )
    return out


def deserialize_json(data: dict) -> LogLocation:
    out: LogLocation = {}  # type: ignore[typeddict-item]
    if "logType" in data:
        import capo_securityagent.types.log_type

        out["log_type"] = capo_securityagent.types.log_type.deserialize_json(
            data["logType"]
        )
    if "cloudWatchLog" in data:
        import capo_securityagent.types.cloud_watch_log

        out["cloud_watch_log"] = (
            capo_securityagent.types.cloud_watch_log.deserialize_json(
                data["cloudWatchLog"]
            )
        )
    return out
