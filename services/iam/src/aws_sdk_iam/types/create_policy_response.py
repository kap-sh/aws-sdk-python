"""Generated from Smithy shape ``com.amazonaws.iam#CreatePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.policy


class CreatePolicyResponse(TypedDict):
    policy: NotRequired["aws_sdk_iam.types.policy.Policy"]
    """<p>A structure containing details about the new policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreatePolicyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "policy" in value:
        import aws_sdk_iam.types.policy

        aws_sdk_iam.types.policy.serialize_query(
            value["policy"], pairs, f"{prefix}.Policy"
        )


def deserialize_query(el: Element) -> CreatePolicyResponse:
    out: CreatePolicyResponse = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        import aws_sdk_iam.types.policy

        out["policy"] = aws_sdk_iam.types.policy.deserialize_query(child_policy)
    return out
