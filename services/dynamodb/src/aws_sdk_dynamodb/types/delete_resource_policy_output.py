"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteResourcePolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.policy_revision_id


class DeleteResourcePolicyOutput(TypedDict):
    revision_id: NotRequired[
        "aws_sdk_dynamodb.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>A unique string that represents the revision ID of the policy. If you're comparing revision IDs, make sure to always use string comparison logic.</p> <p>This value will be empty if you make a request against a resource without a policy.</p>"""
