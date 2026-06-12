"""Generated from Smithy shape ``com.amazonaws.xray#ResourcePolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.policy_document
    import aws_sdk_xray.types.policy_name
    import aws_sdk_xray.types.policy_revision_id
    import aws_sdk_xray.types.timestamp


class ResourcePolicy(TypedDict):
    policy_name: NotRequired["aws_sdk_xray.types.policy_name.PolicyName"]
    """<p>The name of the resource policy. Must be unique within a specific Amazon Web Services account.</p>"""
    policy_document: NotRequired["aws_sdk_xray.types.policy_document.PolicyDocument"]
    """<p>The resource policy document, which can be up to 5kb in size.</p>"""
    policy_revision_id: NotRequired[
        "aws_sdk_xray.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>Returns the current policy revision id for this policy name.</p>"""
    last_updated_time: NotRequired["aws_sdk_xray.types.timestamp.Timestamp"]
    """<p>When the policy was last updated, in Unix time seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePolicy) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    if "policy_document" in value:
        out["PolicyDocument"] = value["policy_document"]
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    if "last_updated_time" in value:
        import aws_sdk_xray.types.timestamp

        out["LastUpdatedTime"] = aws_sdk_xray.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> ResourcePolicy:
    out: ResourcePolicy = {}  # type: ignore[typeddict-item]
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    if "PolicyDocument" in data:
        out["policy_document"] = data["PolicyDocument"]
    if "PolicyRevisionId" in data:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    if "LastUpdatedTime" in data:
        import aws_sdk_xray.types.timestamp

        out["last_updated_time"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    return out
