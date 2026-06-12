"""Generated from Smithy shape ``com.amazonaws.ecr#SetRepositoryPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.force_flag
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name
    import aws_sdk_ecr.types.repository_policy_text


class SetRepositoryPolicyRequest(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "aws_sdk_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository to receive the policy.</p>"""
    policy_text: "aws_sdk_ecr.types.repository_policy_text.RepositoryPolicyText"
    """<p>The JSON repository policy text to apply to the repository. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html\">Amazon ECR repository policies</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>"""
    force: "aws_sdk_ecr.types.force_flag.ForceFlag"
    """<p>If the policy you are attempting to set on a repository policy would prevent you from setting another policy in the future, you must force the <a>SetRepositoryPolicy</a> operation. This is intended to prevent accidental repository lock outs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetRepositoryPolicyRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    out["policyText"] = value["policy_text"]
    out["force"] = value.get("force", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> SetRepositoryPolicyRequest:
    out: SetRepositoryPolicyRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "SetRepositoryPolicyRequest.repository_name required"
        )
    if "policyText" in data:
        out["policy_text"] = data["policyText"]
    else:
        raise DeserializationError("SetRepositoryPolicyRequest.policy_text required")
    if "force" in data:
        out["force"] = data["force"]
    else:
        out["force"] = False
    return out
