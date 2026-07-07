"""Generated from Smithy shape ``com.amazonaws.m2#LogGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.log_group_identifier
    import aws_sdk_m2.types.string20


class LogGroupSummary(TypedDict, closed=True):
    log_type: "aws_sdk_m2.types.string20.String20"
    """<p>The type of log.</p>"""
    log_group_name: "aws_sdk_m2.types.log_group_identifier.LogGroupIdentifier"
    """<p>The name of the log group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogGroupSummary) -> dict:
    out: dict = {}
    out["logType"] = value["log_type"]
    out["logGroupName"] = value["log_group_name"]
    return out


def deserialize_json(data: dict) -> LogGroupSummary:
    out: LogGroupSummary = {}  # type: ignore[typeddict-item]
    if "logType" in data:
        out["log_type"] = data["logType"]
    else:
        raise DeserializationError("LogGroupSummary.log_type required")
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("LogGroupSummary.log_group_name required")
    return out
