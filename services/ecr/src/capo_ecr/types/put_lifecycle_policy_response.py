"""Generated from Smithy shape ``com.amazonaws.ecr#PutLifecyclePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.lifecycle_policy_text
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class PutLifecyclePolicyResponse(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_name: NotRequired["capo_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the request.</p>"""
    lifecycle_policy_text: NotRequired[
        "capo_ecr.types.lifecycle_policy_text.LifecyclePolicyText"
    ]
    """<p>The JSON repository policy text.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutLifecyclePolicyResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "lifecycle_policy_text" in value:
        out["lifecyclePolicyText"] = value["lifecycle_policy_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutLifecyclePolicyResponse:
    out: PutLifecyclePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    if data.get("lifecyclePolicyText") is not None:
        out["lifecycle_policy_text"] = data["lifecyclePolicyText"]
    return out
