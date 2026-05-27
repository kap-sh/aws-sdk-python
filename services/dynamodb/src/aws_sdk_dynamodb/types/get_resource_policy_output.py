"""Generated from Smithy shape ``com.amazonaws.dynamodb#GetResourcePolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.policy_revision_id
    import aws_sdk_dynamodb.types.resource_policy


class GetResourcePolicyOutput(TypedDict):
    policy: NotRequired["aws_sdk_dynamodb.types.resource_policy.ResourcePolicy"]
    """<p>The resource-based policy document attached to the resource, which can be a table or stream, in JSON format.</p>"""
    revision_id: NotRequired[
        "aws_sdk_dynamodb.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>A unique string that represents the revision ID of the policy. If you're comparing revision IDs, make sure to always use string comparison logic.</p>"""
