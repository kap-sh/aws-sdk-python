"""Generated from Smithy shape ``com.amazonaws.ecrpublic#GetRepositoryPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.registry_id
    import aws_sdk_ecr_public.types.repository_name
    import aws_sdk_ecr_public.types.repository_policy_text


class GetRepositoryPolicyResponse(TypedDict, closed=True):
    registry_id: NotRequired["aws_sdk_ecr_public.types.registry_id.RegistryId"]
    """<p>The registry ID that's associated with the request.</p>"""
    repository_name: NotRequired[
        "aws_sdk_ecr_public.types.repository_name.RepositoryName"
    ]
    """<p>The repository name that's associated with the request.</p>"""
    policy_text: NotRequired[
        "aws_sdk_ecr_public.types.repository_policy_text.RepositoryPolicyText"
    ]
    """<p>The repository policy text that's associated with the repository. The policy text will be in JSON format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRepositoryPolicyResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "policy_text" in value:
        out["policyText"] = value["policy_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRepositoryPolicyResponse:
    out: GetRepositoryPolicyResponse = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "policyText" in data:
        out["policy_text"] = data["policyText"]
    return out
