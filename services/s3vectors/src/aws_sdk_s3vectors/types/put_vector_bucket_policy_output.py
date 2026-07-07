"""Generated from Smithy shape ``com.amazonaws.s3vectors#PutVectorBucketPolicyOutput``."""

from typing_extensions import TypedDict


class PutVectorBucketPolicyOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutVectorBucketPolicyOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutVectorBucketPolicyOutput:
    out: PutVectorBucketPolicyOutput = {}  # type: ignore[typeddict-item]
    return out
