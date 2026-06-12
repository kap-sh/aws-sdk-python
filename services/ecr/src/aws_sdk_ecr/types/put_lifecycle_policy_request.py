"""Generated from Smithy shape ``com.amazonaws.ecr#PutLifecyclePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.lifecycle_policy_text
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class PutLifecyclePolicyRequest(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "aws_sdk_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository to receive the policy.</p>"""
    lifecycle_policy_text: "aws_sdk_ecr.types.lifecycle_policy_text.LifecyclePolicyText"
    """<p>The JSON repository policy text to apply to the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutLifecyclePolicyRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    out["lifecyclePolicyText"] = value["lifecycle_policy_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutLifecyclePolicyRequest:
    out: PutLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("PutLifecyclePolicyRequest.repository_name required")
    if "lifecyclePolicyText" in data:
        out["lifecycle_policy_text"] = data["lifecyclePolicyText"]
    else:
        raise DeserializationError(
            "PutLifecyclePolicyRequest.lifecycle_policy_text required"
        )
    return out
