"""Generated from Smithy shape ``com.amazonaws.ecs#TaskEphemeralStorage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.integer
    import capo_ecs.types.string


class TaskEphemeralStorage(TypedDict, closed=True):
    size_in_gi_b: "capo_ecs.types.integer.Integer"
    """<p>The total amount, in GiB, of the ephemeral storage to set for the task. The minimum supported value is <code>20</code> GiB and the maximum supported value is <code>200</code> GiB.</p>"""
    kms_key_id: NotRequired["capo_ecs.types.string.String"]
    """<p>Specify an Key Management Service key ID to encrypt the ephemeral storage for the task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskEphemeralStorage) -> dict:
    out: dict = {}
    out["sizeInGiB"] = value.get("size_in_gi_b", 0)
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskEphemeralStorage:
    out: TaskEphemeralStorage = {}  # type: ignore[typeddict-item]
    if "sizeInGiB" in data:
        out["size_in_gi_b"] = data["sizeInGiB"]
    else:
        out["size_in_gi_b"] = 0
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
