"""Generated from Smithy shape ``com.amazonaws.odb#DatabaseTool``."""

from typing_extensions import NotRequired, TypedDict


class DatabaseTool(TypedDict, closed=True):
    is_enabled: NotRequired["bool"]
    """<p>Indicates whether the database management tool is enabled.</p>"""
    name: NotRequired["str"]
    """<p>The name of the database management tool.</p>"""
    compute_count: NotRequired["float"]
    """<p>The compute capacity allocated to the database management tool.</p>"""
    max_idle_time_in_minutes: NotRequired["int"]
    """<p>The maximum amount of time, in minutes, that the database management tool can be idle before it is shut down.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatabaseTool) -> dict:
    out: dict = {}
    if "is_enabled" in value:
        out["isEnabled"] = value["is_enabled"]
    if "name" in value:
        out["name"] = value["name"]
    if "compute_count" in value:
        out["computeCount"] = value["compute_count"]
    if "max_idle_time_in_minutes" in value:
        out["maxIdleTimeInMinutes"] = value["max_idle_time_in_minutes"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DatabaseTool:
    out: DatabaseTool = {}  # type: ignore[typeddict-item]
    if "isEnabled" in data:
        out["is_enabled"] = data["isEnabled"]
    if "name" in data:
        out["name"] = data["name"]
    if "computeCount" in data:
        out["compute_count"] = data["computeCount"]
    if "maxIdleTimeInMinutes" in data:
        out["max_idle_time_in_minutes"] = data["maxIdleTimeInMinutes"]
    return out
