"""Generated from Smithy shape ``com.amazonaws.iot#ListPolicyVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.policy_versions


class ListPolicyVersionsResponse(TypedDict):
    policy_versions: NotRequired["aws_sdk_iot.types.policy_versions.PolicyVersions"]
    """<p>The policy versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyVersionsResponse) -> dict:
    out: dict = {}
    if "policy_versions" in value:
        import aws_sdk_iot.types.policy_versions

        out["policyVersions"] = aws_sdk_iot.types.policy_versions.serialize_json(
            value["policy_versions"]
        )
    return out


def deserialize_json(data: dict) -> ListPolicyVersionsResponse:
    out: ListPolicyVersionsResponse = {}  # type: ignore[typeddict-item]
    if "policyVersions" in data:
        import aws_sdk_iot.types.policy_versions

        out["policy_versions"] = aws_sdk_iot.types.policy_versions.deserialize_json(
            data["policyVersions"]
        )
    return out
