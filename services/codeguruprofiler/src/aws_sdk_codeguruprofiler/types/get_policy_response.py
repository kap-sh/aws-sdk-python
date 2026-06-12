"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#GetPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.revision_id


class GetPolicyResponse(TypedDict):
    policy: "str"
    """<p>The JSON-formatted resource-based policy attached to the <code>ProfilingGroup</code>.</p>"""
    revision_id: "aws_sdk_codeguruprofiler.types.revision_id.RevisionId"
    """<p>A unique identifier for the current revision of the returned policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyResponse) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> GetPolicyResponse:
    out: GetPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("GetPolicyResponse.policy required")
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    else:
        raise DeserializationError("GetPolicyResponse.revision_id required")
    return out
