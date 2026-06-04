"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentEphemeralStorage``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DeploymentEphemeralStorage(TypedDict):
    kms_key_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Specify an Key Management Service key ID to encrypt the ephemeral storage for deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentEphemeralStorage) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentEphemeralStorage:
    out: DeploymentEphemeralStorage = {}  # type: ignore[typeddict-item]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
