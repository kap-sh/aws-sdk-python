"""Generated from Smithy shape ``com.amazonaws.ecr#DeleteRegistryPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.registry_policy_text


class DeleteRegistryPolicyResponse(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    policy_text: NotRequired[
        "aws_sdk_ecr.types.registry_policy_text.RegistryPolicyText"
    ]
    """<p>The contents of the registry permissions policy that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRegistryPolicyResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "policy_text" in value:
        out["policyText"] = value["policy_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRegistryPolicyResponse:
    out: DeleteRegistryPolicyResponse = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "policyText" in data:
        out["policy_text"] = data["policyText"]
    return out
