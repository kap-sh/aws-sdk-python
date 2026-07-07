"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.expected_revision_id
    import aws_sdk_cloudwatch_logs.types.resource_policy


class PutResourcePolicyResponse(TypedDict, closed=True):
    resource_policy: NotRequired[
        "aws_sdk_cloudwatch_logs.types.resource_policy.ResourcePolicy"
    ]
    """<p>The new policy.</p>"""
    revision_id: NotRequired[
        "aws_sdk_cloudwatch_logs.types.expected_revision_id.ExpectedRevisionId"
    ]
    """<p>The revision ID of the created or updated resource policy. Only returned for resource-scoped policies.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_policy" in value:
        import aws_sdk_cloudwatch_logs.types.resource_policy

        out["resourcePolicy"] = (
            aws_sdk_cloudwatch_logs.types.resource_policy.serialize_aws_json_1_1(
                value["resource_policy"]
            )
        )
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "resourcePolicy" in data:
        import aws_sdk_cloudwatch_logs.types.resource_policy

        out["resource_policy"] = (
            aws_sdk_cloudwatch_logs.types.resource_policy.deserialize_aws_json_1_1(
                data["resourcePolicy"]
            )
        )
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    return out
