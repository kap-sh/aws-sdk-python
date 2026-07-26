"""Generated from Smithy shape ``com.amazonaws.iot#ListPolicyVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.policy_versions


class ListPolicyVersionsResponse(TypedDict, closed=True):
    policy_versions: NotRequired["capo_iot.types.policy_versions.PolicyVersions"]
    """<p>The policy versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyVersionsResponse) -> dict:
    out: dict = {}
    if "policy_versions" in value:
        import capo_iot.types.policy_versions

        out["policyVersions"] = capo_iot.types.policy_versions.serialize_json(
            value["policy_versions"]
        )
    return out


def deserialize_json(data: dict) -> ListPolicyVersionsResponse:
    out: ListPolicyVersionsResponse = {}  # type: ignore[typeddict-item]
    if "policyVersions" in data:
        import capo_iot.types.policy_versions

        out["policy_versions"] = capo_iot.types.policy_versions.deserialize_json(
            data["policyVersions"]
        )
    return out
