"""Generated from Smithy shape ``com.amazonaws.devicefarm#InstallToRemoteAccessSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name


class InstallToRemoteAccessSessionRequest(TypedDict, closed=True):
    remote_access_session_arn: (
        "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the remote access session about which you are requesting information.</p>"""
    app_arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the app about which you are requesting information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstallToRemoteAccessSessionRequest) -> dict:
    out: dict = {}
    out["remoteAccessSessionArn"] = value["remote_access_session_arn"]
    out["appArn"] = value["app_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstallToRemoteAccessSessionRequest:
    out: InstallToRemoteAccessSessionRequest = {}  # type: ignore[typeddict-item]
    if "remoteAccessSessionArn" in data:
        out["remote_access_session_arn"] = data["remoteAccessSessionArn"]
    else:
        raise DeserializationError(
            "InstallToRemoteAccessSessionRequest.remote_access_session_arn required"
        )
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "InstallToRemoteAccessSessionRequest.app_arn required"
        )
    return out
