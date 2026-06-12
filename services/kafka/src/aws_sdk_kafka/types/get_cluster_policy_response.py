"""Generated from Smithy shape ``com.amazonaws.kafka#GetClusterPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class GetClusterPolicyResponse(TypedDict):
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The version of cluster policy.</p>"""
    policy: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The cluster policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClusterPolicyResponse) -> dict:
    out: dict = {}
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetClusterPolicyResponse:
    out: GetClusterPolicyResponse = {}  # type: ignore[typeddict-item]
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "policy" in data:
        out["policy"] = data["policy"]
    return out
