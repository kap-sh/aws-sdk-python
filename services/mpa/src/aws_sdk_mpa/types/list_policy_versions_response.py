"""Generated from Smithy shape ``com.amazonaws.mpa#ListPolicyVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mpa.types.policy_versions
    import aws_sdk_mpa.types.token


class ListPolicyVersionsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_mpa.types.token.Token"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>"""
    policy_versions: NotRequired["aws_sdk_mpa.types.policy_versions.PolicyVersions"]
    """<p>An array of <code>PolicyVersionSummary</code> objects. Contains details for the version of the policies that define the permissions for team resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "policy_versions" in value:
        import aws_sdk_mpa.types.policy_versions

        out["PolicyVersions"] = aws_sdk_mpa.types.policy_versions.serialize_json(
            value["policy_versions"]
        )
    return out


def deserialize_json(data: dict) -> ListPolicyVersionsResponse:
    out: ListPolicyVersionsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PolicyVersions" in data:
        import aws_sdk_mpa.types.policy_versions

        out["policy_versions"] = aws_sdk_mpa.types.policy_versions.deserialize_json(
            data["PolicyVersions"]
        )
    return out
