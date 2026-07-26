"""Generated from Smithy shape ``com.amazonaws.iam#GetPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.policy


class GetPolicyResponse(TypedDict, closed=True):
    policy: NotRequired["capo_iam.types.policy.Policy"]
    """<p>A structure containing details about the policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetPolicyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "policy" in value:
        import capo_iam.types.policy

        capo_iam.types.policy.serialize_query(
            value["policy"], pairs, f"{prefix}.Policy"
        )


def deserialize_query(el: Element) -> GetPolicyResponse:
    out: GetPolicyResponse = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        import capo_iam.types.policy

        out["policy"] = capo_iam.types.policy.deserialize_query(child_policy)
    return out
