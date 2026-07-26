"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.policy_string


class GetResourcePolicyResponse(TypedDict, closed=True):
    policy: NotRequired[
        "capo_migration_hub_refactor_spaces.types.policy_string.PolicyString"
    ]
    """<p>A JSON-formatted string for an Amazon Web Services resource-based policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
