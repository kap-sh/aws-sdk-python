"""Generated from Smithy shape ``com.amazonaws.iam#GetPolicyVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.policy_version


class GetPolicyVersionResponse(TypedDict, closed=True):
    policy_version: NotRequired["aws_sdk_iam.types.policy_version.PolicyVersion"]
    """<p>A structure containing details about the policy version.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetPolicyVersionResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "policy_version" in value:
        import aws_sdk_iam.types.policy_version

        aws_sdk_iam.types.policy_version.serialize_query(
            value["policy_version"], pairs, f"{prefix}.PolicyVersion"
        )


def deserialize_query(el: Element) -> GetPolicyVersionResponse:
    out: GetPolicyVersionResponse = {}  # type: ignore[typeddict-item]
    child_policy_version = el.find("PolicyVersion")
    if child_policy_version is not None:
        import aws_sdk_iam.types.policy_version

        out["policy_version"] = aws_sdk_iam.types.policy_version.deserialize_query(
            child_policy_version
        )
    return out
