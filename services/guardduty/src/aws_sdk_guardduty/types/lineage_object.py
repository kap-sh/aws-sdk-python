"""Generated from Smithy shape ``com.amazonaws.guardduty#LineageObject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.timestamp


class LineageObject(TypedDict):
    start_time: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The time when the process started. This is in UTC format.</p>"""
    namespace_pid: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The process ID of the child process.</p>"""
    user_id: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The user ID of the user that executed the process.</p>"""
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the process.</p>"""
    pid: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The ID of the process.</p>"""
    uuid: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The unique ID assigned to the process by GuardDuty.</p>"""
    executable_path: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The absolute path of the process executable file.</p>"""
    euid: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The effective user ID that was used to execute the process.</p>"""
    parent_uuid: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The unique ID of the parent process. This ID is assigned to the parent process by GuardDuty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageObject) -> dict:
    out: dict = {}
    if "start_time" in value:
        import aws_sdk_guardduty.types.timestamp

        out["startTime"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "namespace_pid" in value:
        out["namespacePid"] = value["namespace_pid"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "pid" in value:
        out["pid"] = value["pid"]
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    if "executable_path" in value:
        out["executablePath"] = value["executable_path"]
    if "euid" in value:
        out["euid"] = value["euid"]
    if "parent_uuid" in value:
        out["parentUuid"] = value["parent_uuid"]
    return out


def deserialize_json(data: dict) -> LineageObject:
    out: LineageObject = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_guardduty.types.timestamp

        out["start_time"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if "namespacePid" in data:
        out["namespace_pid"] = data["namespacePid"]
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "name" in data:
        out["name"] = data["name"]
    if "pid" in data:
        out["pid"] = data["pid"]
    if "uuid" in data:
        out["uuid"] = data["uuid"]
    if "executablePath" in data:
        out["executable_path"] = data["executablePath"]
    if "euid" in data:
        out["euid"] = data["euid"]
    if "parentUuid" in data:
        out["parent_uuid"] = data["parentUuid"]
    return out
