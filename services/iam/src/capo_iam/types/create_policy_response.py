"""Generated from Smithy shape ``com.amazonaws.iam#CreatePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.policy


class CreatePolicyResponse(TypedDict, closed=True):
    policy: NotRequired["capo_iam.types.policy.Policy"]
    """<p>A structure containing details about the new policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreatePolicyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "policy" in value:
        import capo_iam.types.policy

        capo_iam.types.policy.serialize_query(
            value["policy"], pairs, f"{key_prefix}Policy"
        )


def deserialize_query(el: Element) -> CreatePolicyResponse:
    out: CreatePolicyResponse = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        import capo_iam.types.policy

        out["policy"] = capo_iam.types.policy.deserialize_query(child_policy)
    return out
