"""Generated from Smithy shape ``com.amazonaws.glue#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_resource_arn
    import aws_sdk_glue.types.hash_string


class DeleteResourcePolicyRequest(TypedDict):
    policy_hash_condition: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The hash value returned when this policy was set.</p>"""
    resource_arn: NotRequired["aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"]
    """<p>The ARN of the Glue resource for the resource policy to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    if "policy_hash_condition" in value:
        out["PolicyHashCondition"] = value["policy_hash_condition"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "PolicyHashCondition" in data:
        out["policy_hash_condition"] = data["PolicyHashCondition"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    return out
