"""Generated from Smithy shape ``com.amazonaws.dlm#LifecyclePolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dlm.types.default_policy
    import aws_sdk_dlm.types.execution_role_arn
    import aws_sdk_dlm.types.gettable_policy_state_values
    import aws_sdk_dlm.types.policy_arn
    import aws_sdk_dlm.types.policy_description
    import aws_sdk_dlm.types.policy_details
    import aws_sdk_dlm.types.policy_id
    import aws_sdk_dlm.types.status_message
    import aws_sdk_dlm.types.tag_map
    import aws_sdk_dlm.types.timestamp


class LifecyclePolicy(TypedDict):
    policy_id: NotRequired["aws_sdk_dlm.types.policy_id.PolicyId"]
    """<p>The identifier of the lifecycle policy.</p>"""
    description: NotRequired["aws_sdk_dlm.types.policy_description.PolicyDescription"]
    """<p>The description of the lifecycle policy.</p>"""
    state: NotRequired[
        "aws_sdk_dlm.types.gettable_policy_state_values.GettablePolicyStateValues"
    ]
    """<p>The activation state of the lifecycle policy.</p>"""
    status_message: NotRequired["aws_sdk_dlm.types.status_message.StatusMessage"]
    """<p>The description of the status.</p>"""
    execution_role_arn: NotRequired[
        "aws_sdk_dlm.types.execution_role_arn.ExecutionRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.</p>"""
    date_created: NotRequired["aws_sdk_dlm.types.timestamp.Timestamp"]
    """<p>The local date and time when the lifecycle policy was created.</p>"""
    date_modified: NotRequired["aws_sdk_dlm.types.timestamp.Timestamp"]
    """<p>The local date and time when the lifecycle policy was last modified.</p>"""
    policy_details: NotRequired["aws_sdk_dlm.types.policy_details.PolicyDetails"]
    """<p>The configuration of the lifecycle policy</p>"""
    tags: NotRequired["aws_sdk_dlm.types.tag_map.TagMap"]
    """<p>The tags.</p>"""
    policy_arn: NotRequired["aws_sdk_dlm.types.policy_arn.PolicyArn"]
    """<p>The Amazon Resource Name (ARN) of the policy.</p>"""
    default_policy: NotRequired["aws_sdk_dlm.types.default_policy.DefaultPolicy"]
    """<p>Indicates whether the policy is a default lifecycle policy or a custom lifecycle policy.</p> <ul> <li> <p> <code>true</code> - the policy is a default policy.</p> </li> <li> <p> <code>false</code> - the policy is a custom policy.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicy) -> dict:
    out: dict = {}
    if "policy_id" in value:
        out["PolicyId"] = value["policy_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "state" in value:
        import aws_sdk_dlm.types.gettable_policy_state_values

        out["State"] = aws_sdk_dlm.types.gettable_policy_state_values.serialize_json(
            value["state"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "date_created" in value:
        import aws_sdk_dlm.types.timestamp

        out["DateCreated"] = aws_sdk_dlm.types.timestamp.serialize_json(
            value["date_created"]
        )
    if "date_modified" in value:
        import aws_sdk_dlm.types.timestamp

        out["DateModified"] = aws_sdk_dlm.types.timestamp.serialize_json(
            value["date_modified"]
        )
    if "policy_details" in value:
        import aws_sdk_dlm.types.policy_details

        out["PolicyDetails"] = aws_sdk_dlm.types.policy_details.serialize_json(
            value["policy_details"]
        )
    if "tags" in value:
        import aws_sdk_dlm.types.tag_map

        out["Tags"] = aws_sdk_dlm.types.tag_map.serialize_json(value["tags"])
    if "policy_arn" in value:
        out["PolicyArn"] = value["policy_arn"]
    if "default_policy" in value:
        out["DefaultPolicy"] = value["default_policy"]
    return out


def deserialize_json(data: dict) -> LifecyclePolicy:
    out: LifecyclePolicy = {}  # type: ignore[typeddict-item]
    if "PolicyId" in data:
        out["policy_id"] = data["PolicyId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "State" in data:
        import aws_sdk_dlm.types.gettable_policy_state_values

        out["state"] = aws_sdk_dlm.types.gettable_policy_state_values.deserialize_json(
            data["State"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "DateCreated" in data:
        import aws_sdk_dlm.types.timestamp

        out["date_created"] = aws_sdk_dlm.types.timestamp.deserialize_json(
            data["DateCreated"]
        )
    if "DateModified" in data:
        import aws_sdk_dlm.types.timestamp

        out["date_modified"] = aws_sdk_dlm.types.timestamp.deserialize_json(
            data["DateModified"]
        )
    if "PolicyDetails" in data:
        import aws_sdk_dlm.types.policy_details

        out["policy_details"] = aws_sdk_dlm.types.policy_details.deserialize_json(
            data["PolicyDetails"]
        )
    if "Tags" in data:
        import aws_sdk_dlm.types.tag_map

        out["tags"] = aws_sdk_dlm.types.tag_map.deserialize_json(data["Tags"])
    if "PolicyArn" in data:
        out["policy_arn"] = data["PolicyArn"]
    if "DefaultPolicy" in data:
        out["default_policy"] = data["DefaultPolicy"]
    return out
