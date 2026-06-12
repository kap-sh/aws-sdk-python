"""Generated from Smithy shape ``com.amazonaws.rum#CwLog``."""

from typing import TypedDict
from typing_extensions import NotRequired

class CwLog(TypedDict):
    cw_log_enabled: NotRequired["bool"]
    """<p>Indicated whether the app monitor stores copies of the data that RUM collects in CloudWatch Logs.</p>"""
    cw_log_group: NotRequired["str"]
    """<p>The name of the log group where the copies are stored.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CwLog) -> dict:
    out: dict = {}
    if "cw_log_enabled" in value:
        out["CwLogEnabled"] = value["cw_log_enabled"]
    if "cw_log_group" in value:
        out["CwLogGroup"] = value["cw_log_group"]
    return out


def deserialize_json(data: dict) -> CwLog:
    out: CwLog = {}  # type: ignore[typeddict-item]
    if "CwLogEnabled" in data:
        out["cw_log_enabled"] = data["CwLogEnabled"]
    if "CwLogGroup" in data:
        out["cw_log_group"] = data["CwLogGroup"]
    return out