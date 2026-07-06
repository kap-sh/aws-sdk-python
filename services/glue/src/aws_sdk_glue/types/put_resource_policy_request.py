"""Generated from Smithy shape ``com.amazonaws.glue#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.enable_hybrid_values
    import aws_sdk_glue.types.exist_condition
    import aws_sdk_glue.types.glue_resource_arn
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.policy_json_string


class PutResourcePolicyRequest(TypedDict, closed=True):
    policy_in_json: "aws_sdk_glue.types.policy_json_string.PolicyJsonString"
    """<p>Contains the policy document to set, in JSON format.</p>"""
    resource_arn: NotRequired["aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"]
    """<p>Do not use. For internal use only.</p>"""
    policy_hash_condition: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The hash value returned when the previous policy was set using <code>PutResourcePolicy</code>. Its purpose is to prevent concurrent modifications of a policy. Do not use this parameter if no previous policy has been set.</p>"""
    policy_exists_condition: NotRequired[
        "aws_sdk_glue.types.exist_condition.ExistCondition"
    ]
    """<p>A value of <code>MUST_EXIST</code> is used to update a policy. A value of <code>NOT_EXIST</code> is used to create a new policy. If a value of <code>NONE</code> or a null value is used, the call does not depend on the existence of a policy.</p>"""
    enable_hybrid: NotRequired[
        "aws_sdk_glue.types.enable_hybrid_values.EnableHybridValues"
    ]
    """<p>If <code>'TRUE'</code>, indicates that you are using both methods to grant cross-account access to Data Catalog resources:</p> <ul> <li> <p>By directly updating the resource policy with <code>PutResourePolicy</code> </p> </li> <li> <p>By using the <b>Grant permissions</b> command on the Amazon Web Services Management Console.</p> </li> </ul> <p>Must be set to <code>'TRUE'</code> if you have already used the Management Console to grant cross-account access, otherwise the call fails. Default is 'FALSE'.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["PolicyInJson"] = value["policy_in_json"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "policy_hash_condition" in value:
        out["PolicyHashCondition"] = value["policy_hash_condition"]
    if "policy_exists_condition" in value:
        import aws_sdk_glue.types.exist_condition

        out["PolicyExistsCondition"] = (
            aws_sdk_glue.types.exist_condition.serialize_aws_json_1_1(
                value["policy_exists_condition"]
            )
        )
    if "enable_hybrid" in value:
        import aws_sdk_glue.types.enable_hybrid_values

        out["EnableHybrid"] = (
            aws_sdk_glue.types.enable_hybrid_values.serialize_aws_json_1_1(
                value["enable_hybrid"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "PolicyInJson" in data:
        out["policy_in_json"] = data["PolicyInJson"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.policy_in_json required")
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "PolicyHashCondition" in data:
        out["policy_hash_condition"] = data["PolicyHashCondition"]
    if "PolicyExistsCondition" in data:
        import aws_sdk_glue.types.exist_condition

        out["policy_exists_condition"] = (
            aws_sdk_glue.types.exist_condition.deserialize_aws_json_1_1(
                data["PolicyExistsCondition"]
            )
        )
    if "EnableHybrid" in data:
        import aws_sdk_glue.types.enable_hybrid_values

        out["enable_hybrid"] = (
            aws_sdk_glue.types.enable_hybrid_values.deserialize_aws_json_1_1(
                data["EnableHybrid"]
            )
        )
    return out
