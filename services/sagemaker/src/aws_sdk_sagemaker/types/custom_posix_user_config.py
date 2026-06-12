"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomPosixUserConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.gid
    import aws_sdk_sagemaker.types.uid


class CustomPosixUserConfig(TypedDict):
    uid: NotRequired["aws_sdk_sagemaker.types.uid.Uid"]
    """<p>The POSIX user ID.</p>"""
    gid: NotRequired["aws_sdk_sagemaker.types.gid.Gid"]
    """<p>The POSIX group ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomPosixUserConfig) -> dict:
    out: dict = {}
    if "uid" in value:
        out["Uid"] = value["uid"]
    if "gid" in value:
        out["Gid"] = value["gid"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomPosixUserConfig:
    out: CustomPosixUserConfig = {}  # type: ignore[typeddict-item]
    if "Uid" in data:
        out["uid"] = data["Uid"]
    if "Gid" in data:
        out["gid"] = data["Gid"]
    return out
