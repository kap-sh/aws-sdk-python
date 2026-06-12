"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#RemoteSourceCodeAnalysisServerInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.string


class RemoteSourceCodeAnalysisServerInfo(TypedDict):
    remote_source_code_analysis_server_configuration_timestamp: NotRequired[
        "aws_sdk_migrationhubstrategy.types.string.String"
    ]
    """<p>The time when the remote source code server was configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteSourceCodeAnalysisServerInfo) -> dict:
    out: dict = {}
    if "remote_source_code_analysis_server_configuration_timestamp" in value:
        out["remoteSourceCodeAnalysisServerConfigurationTimestamp"] = value[
            "remote_source_code_analysis_server_configuration_timestamp"
        ]
    return out


def deserialize_json(data: dict) -> RemoteSourceCodeAnalysisServerInfo:
    out: RemoteSourceCodeAnalysisServerInfo = {}  # type: ignore[typeddict-item]
    if "remoteSourceCodeAnalysisServerConfigurationTimestamp" in data:
        out["remote_source_code_analysis_server_configuration_timestamp"] = data[
            "remoteSourceCodeAnalysisServerConfigurationTimestamp"
        ]
    return out
