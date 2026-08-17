"""Generated from Smithy shape ``com.amazonaws.lambda#GetPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.string


class GetPolicyResponse(TypedDict, closed=True):
    policy: NotRequired["capo_lambda.types.string.String"]
    """<p>The resource-based policy.</p>"""
    revision_id: NotRequired["capo_lambda.types.string.String"]
    """<p>A unique identifier for the current revision of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> GetPolicyResponse:
    out: GetPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    return out
