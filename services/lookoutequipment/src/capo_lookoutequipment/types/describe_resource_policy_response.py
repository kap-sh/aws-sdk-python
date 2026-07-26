"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.policy
    import capo_lookoutequipment.types.policy_revision_id
    import capo_lookoutequipment.types.timestamp


class DescribeResourcePolicyResponse(TypedDict, closed=True):
    policy_revision_id: NotRequired[
        "capo_lookoutequipment.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>A unique identifier for a revision of the resource policy.</p>"""
    resource_policy: NotRequired["capo_lookoutequipment.types.policy.Policy"]
    """<p>The resource policy in a JSON-formatted string.</p>"""
    creation_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>The time when the resource policy was created.</p>"""
    last_modified_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>The time when the resource policy was last modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    if "resource_policy" in value:
        out["ResourcePolicy"] = value["resource_policy"]
    if "creation_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["CreationTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["LastModifiedTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeResourcePolicyResponse:
    out: DescribeResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "PolicyRevisionId" in data:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    if "ResourcePolicy" in data:
        out["resource_policy"] = data["ResourcePolicy"]
    if "CreationTime" in data:
        import capo_lookoutequipment.types.timestamp

        out["creation_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_lookoutequipment.types.timestamp

        out["last_modified_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["LastModifiedTime"]
            )
        )
    return out
