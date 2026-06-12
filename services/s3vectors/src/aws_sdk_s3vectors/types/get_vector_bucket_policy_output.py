"""Generated from Smithy shape ``com.amazonaws.s3vectors#GetVectorBucketPolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.vector_bucket_policy

class GetVectorBucketPolicyOutput(TypedDict):
    policy: NotRequired["aws_sdk_s3vectors.types.vector_bucket_policy.VectorBucketPolicy"]
    """<p>The <code>JSON</code> that defines the policy.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetVectorBucketPolicyOutput) -> dict:
    out: dict = {}
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetVectorBucketPolicyOutput:
    out: GetVectorBucketPolicyOutput = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        out["policy"] = data["policy"]
    return out