"""Generated from Smithy shape ``com.amazonaws.ecr#UpdatePullThroughCacheRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.credential_arn
    import capo_ecr.types.custom_role_arn
    import capo_ecr.types.pull_through_cache_rule_repository_prefix
    import capo_ecr.types.registry_id
    import capo_ecr.types.updated_timestamp


class UpdatePullThroughCacheRuleResponse(TypedDict, closed=True):
    ecr_repository_prefix: NotRequired[
        "capo_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix"
    ]
    """<p>The Amazon ECR repository prefix associated with the pull through cache rule.</p>"""
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    updated_at: NotRequired["capo_ecr.types.updated_timestamp.UpdatedTimestamp"]
    """<p>The date and time, in JavaScript date format, when the pull through cache rule was updated.</p>"""
    credential_arn: NotRequired["capo_ecr.types.credential_arn.CredentialArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret associated with the pull through cache rule.</p>"""
    custom_role_arn: NotRequired["capo_ecr.types.custom_role_arn.CustomRoleArn"]
    """<p>The ARN of the IAM role associated with the pull through cache rule.</p>"""
    upstream_repository_prefix: NotRequired[
        "capo_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix"
    ]
    """<p>The upstream repository prefix associated with the pull through cache rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePullThroughCacheRuleResponse) -> dict:
    out: dict = {}
    if "ecr_repository_prefix" in value:
        out["ecrRepositoryPrefix"] = value["ecr_repository_prefix"]
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "updated_at" in value:
        import capo_ecr.types.updated_timestamp

        out["updatedAt"] = capo_ecr.types.updated_timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "credential_arn" in value:
        out["credentialArn"] = value["credential_arn"]
    if "custom_role_arn" in value:
        out["customRoleArn"] = value["custom_role_arn"]
    if "upstream_repository_prefix" in value:
        out["upstreamRepositoryPrefix"] = value["upstream_repository_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePullThroughCacheRuleResponse:
    out: UpdatePullThroughCacheRuleResponse = {}  # type: ignore[typeddict-item]
    if "ecrRepositoryPrefix" in data:
        out["ecr_repository_prefix"] = data["ecrRepositoryPrefix"]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "updatedAt" in data:
        import capo_ecr.types.updated_timestamp

        out["updated_at"] = capo_ecr.types.updated_timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    if "credentialArn" in data:
        out["credential_arn"] = data["credentialArn"]
    if "customRoleArn" in data:
        out["custom_role_arn"] = data["customRoleArn"]
    if "upstreamRepositoryPrefix" in data:
        out["upstream_repository_prefix"] = data["upstreamRepositoryPrefix"]
    return out
