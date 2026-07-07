"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcrRepositoryLifecyclePolicyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcrRepositoryLifecyclePolicyDetails(TypedDict, closed=True):
    lifecycle_policy_text: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The text of the lifecycle policy.</p>"""
    registry_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Web Services account identifier that is associated with the registry that contains the repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcrRepositoryLifecyclePolicyDetails) -> dict:
    out: dict = {}
    if "lifecycle_policy_text" in value:
        out["LifecyclePolicyText"] = value["lifecycle_policy_text"]
    if "registry_id" in value:
        out["RegistryId"] = value["registry_id"]
    return out


def deserialize_json(data: dict) -> AwsEcrRepositoryLifecyclePolicyDetails:
    out: AwsEcrRepositoryLifecyclePolicyDetails = {}  # type: ignore[typeddict-item]
    if "LifecyclePolicyText" in data:
        out["lifecycle_policy_text"] = data["LifecyclePolicyText"]
    if "RegistryId" in data:
        out["registry_id"] = data["RegistryId"]
    return out
