"""Generated from Smithy shape ``com.amazonaws.dynamodb#GetResourcePolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.resource_arn_string


class GetResourcePolicyInput(TypedDict):
    resource_arn: "aws_sdk_dynamodb.types.resource_arn_string.ResourceArnString"
    """<p>The Amazon Resource Name (ARN) of the DynamoDB resource to which the policy is attached. The resources you can specify include tables and streams.</p>"""
