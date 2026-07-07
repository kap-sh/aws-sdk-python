"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#S3FilesAccessPointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.mount_path
    import aws_sdk_bedrock_agentcore_control.types.s3_files_access_point_arn


class S3FilesAccessPointConfiguration(TypedDict, closed=True):
    access_point_arn: "aws_sdk_bedrock_agentcore_control.types.s3_files_access_point_arn.S3FilesAccessPointArn"
    """<p>The ARN of the S3 Files access point to mount into the AgentCore Runtime.</p>"""
    mount_path: "aws_sdk_bedrock_agentcore_control.types.mount_path.MountPath"
    """<p>The mount path for the S3 Files access point inside the AgentCore Runtime. The path must be under <code>/mnt</code> with exactly one subdirectory level (for example, <code>/mnt/data</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3FilesAccessPointConfiguration) -> dict:
    out: dict = {}
    out["accessPointArn"] = value["access_point_arn"]
    out["mountPath"] = value["mount_path"]
    return out


def deserialize_json(data: dict) -> S3FilesAccessPointConfiguration:
    out: S3FilesAccessPointConfiguration = {}  # type: ignore[typeddict-item]
    if "accessPointArn" in data:
        out["access_point_arn"] = data["accessPointArn"]
    else:
        raise DeserializationError(
            "S3FilesAccessPointConfiguration.access_point_arn required"
        )
    if "mountPath" in data:
        out["mount_path"] = data["mountPath"]
    else:
        raise DeserializationError(
            "S3FilesAccessPointConfiguration.mount_path required"
        )
    return out
