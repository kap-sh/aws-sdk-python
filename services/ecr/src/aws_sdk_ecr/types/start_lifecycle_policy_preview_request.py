"""Generated from Smithy shape ``com.amazonaws.ecr#StartLifecyclePolicyPreviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.lifecycle_policy_text
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class StartLifecyclePolicyPreviewRequest(TypedDict, closed=True):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "aws_sdk_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository to be evaluated.</p>"""
    lifecycle_policy_text: NotRequired[
        "aws_sdk_ecr.types.lifecycle_policy_text.LifecyclePolicyText"
    ]
    """<p>The policy to be evaluated against. If you do not specify a policy, the current policy for the repository is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartLifecyclePolicyPreviewRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    if "lifecycle_policy_text" in value:
        out["lifecyclePolicyText"] = value["lifecycle_policy_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartLifecyclePolicyPreviewRequest:
    out: StartLifecyclePolicyPreviewRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "StartLifecyclePolicyPreviewRequest.repository_name required"
        )
    if "lifecyclePolicyText" in data:
        out["lifecycle_policy_text"] = data["lifecyclePolicyText"]
    return out
