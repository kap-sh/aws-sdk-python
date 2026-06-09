"""Generated from Smithy shape ``com.amazonaws.iam#GetPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.policy


class GetPolicyResponse(TypedDict):
    policy: NotRequired["aws_sdk_iam.types.policy.Policy"]
    """<p>A structure containing details about the policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetPolicyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "policy" in value:
        import aws_sdk_iam.types.policy

        aws_sdk_iam.types.policy.serialize_query(
            value["policy"], pairs, f"{prefix}.Policy"
        )


def deserialize_query(el: Element) -> GetPolicyResponse:
    out: GetPolicyResponse = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        import aws_sdk_iam.types.policy

        out["policy"] = aws_sdk_iam.types.policy.deserialize_query(child_policy)
    return out
