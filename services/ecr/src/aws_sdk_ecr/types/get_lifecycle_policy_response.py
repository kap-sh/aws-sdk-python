"""Generated from Smithy shape ``com.amazonaws.ecr#GetLifecyclePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.evaluation_timestamp
    import aws_sdk_ecr.types.lifecycle_policy_text
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class GetLifecyclePolicyResponse(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_name: NotRequired["aws_sdk_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the request.</p>"""
    lifecycle_policy_text: NotRequired[
        "aws_sdk_ecr.types.lifecycle_policy_text.LifecyclePolicyText"
    ]
    """<p>The JSON lifecycle policy text.</p>"""
    last_evaluated_at: NotRequired[
        "aws_sdk_ecr.types.evaluation_timestamp.EvaluationTimestamp"
    ]
    """<p>The time stamp of the last time that the lifecycle policy was run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLifecyclePolicyResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "lifecycle_policy_text" in value:
        out["lifecyclePolicyText"] = value["lifecycle_policy_text"]
    if "last_evaluated_at" in value:
        import aws_sdk_ecr.types.evaluation_timestamp

        out["lastEvaluatedAt"] = (
            aws_sdk_ecr.types.evaluation_timestamp.serialize_aws_json_1_1(
                value["last_evaluated_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLifecyclePolicyResponse:
    out: GetLifecyclePolicyResponse = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "lifecyclePolicyText" in data:
        out["lifecycle_policy_text"] = data["lifecyclePolicyText"]
    if "lastEvaluatedAt" in data:
        import aws_sdk_ecr.types.evaluation_timestamp

        out["last_evaluated_at"] = (
            aws_sdk_ecr.types.evaluation_timestamp.deserialize_aws_json_1_1(
                data["lastEvaluatedAt"]
            )
        )
    return out
