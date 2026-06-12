"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ConfigurationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.ip_address_based_remote_info_list
    import aws_sdk_migrationhubstrategy.types.pipeline_info_list
    import aws_sdk_migrationhubstrategy.types.remote_source_code_analysis_server_info
    import aws_sdk_migrationhubstrategy.types.vcenter_based_remote_info_list
    import aws_sdk_migrationhubstrategy.types.version_control_info_list


class ConfigurationSummary(TypedDict):
    vcenter_based_remote_info_list: NotRequired[
        "aws_sdk_migrationhubstrategy.types.vcenter_based_remote_info_list.VcenterBasedRemoteInfoList"
    ]
    """<p>The list of vCenter configurations.</p>"""
    ip_address_based_remote_info_list: NotRequired[
        "aws_sdk_migrationhubstrategy.types.ip_address_based_remote_info_list.IPAddressBasedRemoteInfoList"
    ]
    """<p>IP address based configurations.</p>"""
    version_control_info_list: NotRequired[
        "aws_sdk_migrationhubstrategy.types.version_control_info_list.VersionControlInfoList"
    ]
    """<p>The list of the version control configurations.</p>"""
    pipeline_info_list: NotRequired[
        "aws_sdk_migrationhubstrategy.types.pipeline_info_list.PipelineInfoList"
    ]
    """<p>The list of pipeline info configurations.</p>"""
    remote_source_code_analysis_server_info: NotRequired[
        "aws_sdk_migrationhubstrategy.types.remote_source_code_analysis_server_info.RemoteSourceCodeAnalysisServerInfo"
    ]
    """<p>Info about the remote server source code configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationSummary) -> dict:
    out: dict = {}
    if "vcenter_based_remote_info_list" in value:
        import aws_sdk_migrationhubstrategy.types.vcenter_based_remote_info_list

        out["vcenterBasedRemoteInfoList"] = (
            aws_sdk_migrationhubstrategy.types.vcenter_based_remote_info_list.serialize_json(
                value["vcenter_based_remote_info_list"]
            )
        )
    if "ip_address_based_remote_info_list" in value:
        import aws_sdk_migrationhubstrategy.types.ip_address_based_remote_info_list

        out["ipAddressBasedRemoteInfoList"] = (
            aws_sdk_migrationhubstrategy.types.ip_address_based_remote_info_list.serialize_json(
                value["ip_address_based_remote_info_list"]
            )
        )
    if "version_control_info_list" in value:
        import aws_sdk_migrationhubstrategy.types.version_control_info_list

        out["versionControlInfoList"] = (
            aws_sdk_migrationhubstrategy.types.version_control_info_list.serialize_json(
                value["version_control_info_list"]
            )
        )
    if "pipeline_info_list" in value:
        import aws_sdk_migrationhubstrategy.types.pipeline_info_list

        out["pipelineInfoList"] = (
            aws_sdk_migrationhubstrategy.types.pipeline_info_list.serialize_json(
                value["pipeline_info_list"]
            )
        )
    if "remote_source_code_analysis_server_info" in value:
        import aws_sdk_migrationhubstrategy.types.remote_source_code_analysis_server_info

        out["remoteSourceCodeAnalysisServerInfo"] = (
            aws_sdk_migrationhubstrategy.types.remote_source_code_analysis_server_info.serialize_json(
                value["remote_source_code_analysis_server_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurationSummary:
    out: ConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "vcenterBasedRemoteInfoList" in data:
        import aws_sdk_migrationhubstrategy.types.vcenter_based_remote_info_list

        out["vcenter_based_remote_info_list"] = (
            aws_sdk_migrationhubstrategy.types.vcenter_based_remote_info_list.deserialize_json(
                data["vcenterBasedRemoteInfoList"]
            )
        )
    if "ipAddressBasedRemoteInfoList" in data:
        import aws_sdk_migrationhubstrategy.types.ip_address_based_remote_info_list

        out["ip_address_based_remote_info_list"] = (
            aws_sdk_migrationhubstrategy.types.ip_address_based_remote_info_list.deserialize_json(
                data["ipAddressBasedRemoteInfoList"]
            )
        )
    if "versionControlInfoList" in data:
        import aws_sdk_migrationhubstrategy.types.version_control_info_list

        out["version_control_info_list"] = (
            aws_sdk_migrationhubstrategy.types.version_control_info_list.deserialize_json(
                data["versionControlInfoList"]
            )
        )
    if "pipelineInfoList" in data:
        import aws_sdk_migrationhubstrategy.types.pipeline_info_list

        out["pipeline_info_list"] = (
            aws_sdk_migrationhubstrategy.types.pipeline_info_list.deserialize_json(
                data["pipelineInfoList"]
            )
        )
    if "remoteSourceCodeAnalysisServerInfo" in data:
        import aws_sdk_migrationhubstrategy.types.remote_source_code_analysis_server_info

        out["remote_source_code_analysis_server_info"] = (
            aws_sdk_migrationhubstrategy.types.remote_source_code_analysis_server_info.deserialize_json(
                data["remoteSourceCodeAnalysisServerInfo"]
            )
        )
    return out
