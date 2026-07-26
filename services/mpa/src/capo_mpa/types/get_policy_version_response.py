"""Generated from Smithy shape ``com.amazonaws.mpa#GetPolicyVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mpa.types.policy_version


class GetPolicyVersionResponse(TypedDict, closed=True):
    policy_version: "capo_mpa.types.policy_version.PolicyVersion"
    """<p>A <code>PolicyVersion</code> object. Contains details for the version of the policy. Policies define the permissions for team resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyVersionResponse) -> dict:
    out: dict = {}
    import capo_mpa.types.policy_version

    out["PolicyVersion"] = capo_mpa.types.policy_version.serialize_json(
        value["policy_version"]
    )
    return out


def deserialize_json(data: dict) -> GetPolicyVersionResponse:
    out: GetPolicyVersionResponse = {}  # type: ignore[typeddict-item]
    if "PolicyVersion" in data:
        import capo_mpa.types.policy_version

        out["policy_version"] = capo_mpa.types.policy_version.deserialize_json(
            data["PolicyVersion"]
        )
    else:
        raise DeserializationError("GetPolicyVersionResponse.policy_version required")
    return out
