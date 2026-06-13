"""Generated from Smithy shape ``com.amazonaws.dsql#DeleteClusterPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dsql.types.client_token
    import aws_sdk_dsql.types.cluster_id
    import aws_sdk_dsql.types.policy_version


class DeleteClusterPolicyInput(TypedDict):
    identifier: "aws_sdk_dsql.types.cluster_id.ClusterId"
    expected_policy_version: NotRequired[
        "aws_sdk_dsql.types.policy_version.PolicyVersion"
    ]
    """<p>The expected version of the policy to delete. This parameter ensures that you're deleting the correct version of the policy and helps prevent accidental deletions.</p>"""
    client_token: NotRequired["aws_sdk_dsql.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterPolicyInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteClusterPolicyInput:
    out: DeleteClusterPolicyInput = {}  # type: ignore[typeddict-item]
    return out
