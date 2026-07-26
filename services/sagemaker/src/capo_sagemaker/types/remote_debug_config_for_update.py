"""Generated from Smithy shape ``com.amazonaws.sagemaker#RemoteDebugConfigForUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.enable_remote_debug


class RemoteDebugConfigForUpdate(TypedDict, closed=True):
    enable_remote_debug: NotRequired[
        "capo_sagemaker.types.enable_remote_debug.EnableRemoteDebug"
    ]
    """<p>If set to True, enables remote debugging.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoteDebugConfigForUpdate) -> dict:
    out: dict = {}
    if "enable_remote_debug" in value:
        out["EnableRemoteDebug"] = value["enable_remote_debug"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoteDebugConfigForUpdate:
    out: RemoteDebugConfigForUpdate = {}  # type: ignore[typeddict-item]
    if "EnableRemoteDebug" in data:
        out["enable_remote_debug"] = data["EnableRemoteDebug"]
    return out
