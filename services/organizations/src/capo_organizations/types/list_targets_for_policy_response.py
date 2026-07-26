"""Generated from Smithy shape ``com.amazonaws.organizations#ListTargetsForPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.next_token
    import capo_organizations.types.policy_targets


class ListTargetsForPolicyResponse(TypedDict, closed=True):
    targets: NotRequired["capo_organizations.types.policy_targets.PolicyTargets"]
    """<p>A list of structures, each of which contains details about one of the entities to which the specified policy is attached.</p>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTargetsForPolicyResponse) -> dict:
    out: dict = {}
    if "targets" in value:
        import capo_organizations.types.policy_targets

        out["Targets"] = capo_organizations.types.policy_targets.serialize_aws_json_1_1(
            value["targets"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTargetsForPolicyResponse:
    out: ListTargetsForPolicyResponse = {}  # type: ignore[typeddict-item]
    if "Targets" in data:
        import capo_organizations.types.policy_targets

        out["targets"] = (
            capo_organizations.types.policy_targets.deserialize_aws_json_1_1(
                data["Targets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
