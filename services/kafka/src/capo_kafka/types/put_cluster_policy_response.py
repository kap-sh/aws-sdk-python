"""Generated from Smithy shape ``com.amazonaws.kafka#PutClusterPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class PutClusterPolicyResponse(TypedDict, closed=True):
    current_version: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The policy version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutClusterPolicyResponse) -> dict:
    out: dict = {}
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    return out


def deserialize_json(data: dict) -> PutClusterPolicyResponse:
    out: PutClusterPolicyResponse = {}  # type: ignore[typeddict-item]
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    return out
