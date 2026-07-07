"""Generated from Smithy shape ``com.amazonaws.sagemaker#RemoteDebugConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.enable_remote_debug


class RemoteDebugConfig(TypedDict, closed=True):
    enable_remote_debug: NotRequired[
        "aws_sdk_sagemaker.types.enable_remote_debug.EnableRemoteDebug"
    ]
    """<p>If set to True, enables remote debugging.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoteDebugConfig) -> dict:
    out: dict = {}
    if "enable_remote_debug" in value:
        out["EnableRemoteDebug"] = value["enable_remote_debug"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoteDebugConfig:
    out: RemoteDebugConfig = {}  # type: ignore[typeddict-item]
    if "EnableRemoteDebug" in data:
        out["enable_remote_debug"] = data["EnableRemoteDebug"]
    return out
