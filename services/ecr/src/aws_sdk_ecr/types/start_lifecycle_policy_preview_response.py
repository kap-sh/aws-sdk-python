"""Generated from Smithy shape ``com.amazonaws.ecr#StartLifecyclePolicyPreviewResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.lifecycle_policy_preview_status
    import aws_sdk_ecr.types.lifecycle_policy_text
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class StartLifecyclePolicyPreviewResponse(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_name: NotRequired["aws_sdk_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the request.</p>"""
    lifecycle_policy_text: NotRequired[
        "aws_sdk_ecr.types.lifecycle_policy_text.LifecyclePolicyText"
    ]
    """<p>The JSON repository policy text.</p>"""
    status: NotRequired[
        "aws_sdk_ecr.types.lifecycle_policy_preview_status.LifecyclePolicyPreviewStatus"
    ]
    """<p>The status of the lifecycle policy preview request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartLifecyclePolicyPreviewResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "lifecycle_policy_text" in value:
        out["lifecyclePolicyText"] = value["lifecycle_policy_text"]
    if "status" in value:
        import aws_sdk_ecr.types.lifecycle_policy_preview_status

        out["status"] = (
            aws_sdk_ecr.types.lifecycle_policy_preview_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartLifecyclePolicyPreviewResponse:
    out: StartLifecyclePolicyPreviewResponse = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "lifecyclePolicyText" in data:
        out["lifecycle_policy_text"] = data["lifecyclePolicyText"]
    if "status" in data:
        import aws_sdk_ecr.types.lifecycle_policy_preview_status

        out["status"] = (
            aws_sdk_ecr.types.lifecycle_policy_preview_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
