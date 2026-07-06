"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#SystemInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.network_info_list
    import aws_sdk_migrationhubstrategy.types.os_info
    import aws_sdk_migrationhubstrategy.types.string


class SystemInfo(TypedDict, closed=True):
    os_info: NotRequired["aws_sdk_migrationhubstrategy.types.os_info.OSInfo"]
    """<p> Operating system corresponding to a server. </p>"""
    file_system_type: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> File system type for the server. </p>"""
    network_info_list: NotRequired[
        "aws_sdk_migrationhubstrategy.types.network_info_list.NetworkInfoList"
    ]
    """<p> Networking information related to a server. </p>"""
    cpu_architecture: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> CPU architecture type for the server. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemInfo) -> dict:
    out: dict = {}
    if "os_info" in value:
        import aws_sdk_migrationhubstrategy.types.os_info

        out["osInfo"] = aws_sdk_migrationhubstrategy.types.os_info.serialize_json(
            value["os_info"]
        )
    if "file_system_type" in value:
        out["fileSystemType"] = value["file_system_type"]
    if "network_info_list" in value:
        import aws_sdk_migrationhubstrategy.types.network_info_list

        out["networkInfoList"] = (
            aws_sdk_migrationhubstrategy.types.network_info_list.serialize_json(
                value["network_info_list"]
            )
        )
    if "cpu_architecture" in value:
        out["cpuArchitecture"] = value["cpu_architecture"]
    return out


def deserialize_json(data: dict) -> SystemInfo:
    out: SystemInfo = {}  # type: ignore[typeddict-item]
    if "osInfo" in data:
        import aws_sdk_migrationhubstrategy.types.os_info

        out["os_info"] = aws_sdk_migrationhubstrategy.types.os_info.deserialize_json(
            data["osInfo"]
        )
    if "fileSystemType" in data:
        out["file_system_type"] = data["fileSystemType"]
    if "networkInfoList" in data:
        import aws_sdk_migrationhubstrategy.types.network_info_list

        out["network_info_list"] = (
            aws_sdk_migrationhubstrategy.types.network_info_list.deserialize_json(
                data["networkInfoList"]
            )
        )
    if "cpuArchitecture" in data:
        out["cpu_architecture"] = data["cpuArchitecture"]
    return out
