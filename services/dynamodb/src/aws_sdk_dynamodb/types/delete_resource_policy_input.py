"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteResourcePolicyInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.policy_revision_id
    import aws_sdk_dynamodb.types.resource_arn_string


class DeleteResourcePolicyInput(TypedDict):
    resource_arn: "aws_sdk_dynamodb.types.resource_arn_string.ResourceArnString"
    """<p>The Amazon Resource Name (ARN) of the DynamoDB resource from which the policy will be removed. The resources you can specify include tables and streams. If you remove the policy of a table, it will also remove the permissions for the table's indexes defined in that policy document. This is because index permissions are defined in the table's policy.</p>"""
    expected_revision_id: NotRequired[
        "aws_sdk_dynamodb.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>A string value that you can use to conditionally delete your policy. When you provide an expected revision ID, if the revision ID of the existing policy on the resource doesn't match or if there's no policy attached to the resource, the request will fail and return a <code>PolicyNotFoundException</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteResourcePolicyInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "expected_revision_id" in value:
        out["ExpectedRevisionId"] = value["expected_revision_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteResourcePolicyInput:
    out: DeleteResourcePolicyInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("DeleteResourcePolicyInput.resource_arn required")
    if "ExpectedRevisionId" in data:
        out["expected_revision_id"] = data["ExpectedRevisionId"]
    return out
