"""Generated from Smithy shape ``com.amazonaws.guardduty#ProcessDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.lineage
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.timestamp


class ProcessDetails(TypedDict):
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the process.</p>"""
    executable_path: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The absolute path of the process executable file.</p>"""
    executable_sha256: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The <code>SHA256</code> hash of the process executable.</p>"""
    namespace_pid: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The ID of the child process.</p>"""
    pwd: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The present working directory of the process.</p>"""
    pid: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The ID of the process.</p>"""
    start_time: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The time when the process started. This is in UTC format.</p>"""
    uuid: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The unique ID assigned to the process by GuardDuty.</p>"""
    parent_uuid: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The unique ID of the parent process. This ID is assigned to the parent process by GuardDuty.</p>"""
    user: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The user that executed the process.</p>"""
    user_id: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The unique ID of the user that executed the process.</p>"""
    euid: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The effective user ID of the user that executed the process.</p>"""
    lineage: NotRequired["aws_sdk_guardduty.types.lineage.Lineage"]
    """<p>Information about the process's lineage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProcessDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "executable_path" in value:
        out["executablePath"] = value["executable_path"]
    if "executable_sha256" in value:
        out["executableSha256"] = value["executable_sha256"]
    if "namespace_pid" in value:
        out["namespacePid"] = value["namespace_pid"]
    if "pwd" in value:
        out["pwd"] = value["pwd"]
    if "pid" in value:
        out["pid"] = value["pid"]
    if "start_time" in value:
        import aws_sdk_guardduty.types.timestamp

        out["startTime"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    if "parent_uuid" in value:
        out["parentUuid"] = value["parent_uuid"]
    if "user" in value:
        out["user"] = value["user"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "euid" in value:
        out["euid"] = value["euid"]
    if "lineage" in value:
        import aws_sdk_guardduty.types.lineage

        out["lineage"] = aws_sdk_guardduty.types.lineage.serialize_json(
            value["lineage"]
        )
    return out


def deserialize_json(data: dict) -> ProcessDetails:
    out: ProcessDetails = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "executablePath" in data:
        out["executable_path"] = data["executablePath"]
    if "executableSha256" in data:
        out["executable_sha256"] = data["executableSha256"]
    if "namespacePid" in data:
        out["namespace_pid"] = data["namespacePid"]
    if "pwd" in data:
        out["pwd"] = data["pwd"]
    if "pid" in data:
        out["pid"] = data["pid"]
    if "startTime" in data:
        import aws_sdk_guardduty.types.timestamp

        out["start_time"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if "uuid" in data:
        out["uuid"] = data["uuid"]
    if "parentUuid" in data:
        out["parent_uuid"] = data["parentUuid"]
    if "user" in data:
        out["user"] = data["user"]
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "euid" in data:
        out["euid"] = data["euid"]
    if "lineage" in data:
        import aws_sdk_guardduty.types.lineage

        out["lineage"] = aws_sdk_guardduty.types.lineage.deserialize_json(
            data["lineage"]
        )
    return out
