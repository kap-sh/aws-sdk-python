"""Generated from Smithy shape ``com.amazonaws.ecr#PullThroughCacheRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.creation_timestamp
    import aws_sdk_ecr.types.credential_arn
    import aws_sdk_ecr.types.custom_role_arn
    import aws_sdk_ecr.types.pull_through_cache_rule_repository_prefix
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.updated_timestamp
    import aws_sdk_ecr.types.upstream_registry
    import aws_sdk_ecr.types.url


class PullThroughCacheRule(TypedDict, closed=True):
    ecr_repository_prefix: NotRequired[
        "aws_sdk_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix"
    ]
    """<p>The Amazon ECR repository prefix associated with the pull through cache rule.</p>"""
    upstream_registry_url: NotRequired["aws_sdk_ecr.types.url.Url"]
    """<p>The upstream registry URL associated with the pull through cache rule.</p>"""
    created_at: NotRequired["aws_sdk_ecr.types.creation_timestamp.CreationTimestamp"]
    """<p>The date and time the pull through cache was created.</p>"""
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry the pull through cache rule is associated with.</p>"""
    credential_arn: NotRequired["aws_sdk_ecr.types.credential_arn.CredentialArn"]
    """<p>The ARN of the Secrets Manager secret associated with the pull through cache rule.</p>"""
    custom_role_arn: NotRequired["aws_sdk_ecr.types.custom_role_arn.CustomRoleArn"]
    """<p>The ARN of the IAM role associated with the pull through cache rule.</p>"""
    upstream_repository_prefix: NotRequired[
        "aws_sdk_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix"
    ]
    """<p>The upstream repository prefix associated with the pull through cache rule.</p>"""
    upstream_registry: NotRequired[
        "aws_sdk_ecr.types.upstream_registry.UpstreamRegistry"
    ]
    """<p>The name of the upstream source registry associated with the pull through cache rule.</p>"""
    updated_at: NotRequired["aws_sdk_ecr.types.updated_timestamp.UpdatedTimestamp"]
    """<p>The date and time, in JavaScript date format, when the pull through cache rule was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullThroughCacheRule) -> dict:
    out: dict = {}
    if "ecr_repository_prefix" in value:
        out["ecrRepositoryPrefix"] = value["ecr_repository_prefix"]
    if "upstream_registry_url" in value:
        out["upstreamRegistryUrl"] = value["upstream_registry_url"]
    if "created_at" in value:
        import aws_sdk_ecr.types.creation_timestamp

        out["createdAt"] = aws_sdk_ecr.types.creation_timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "credential_arn" in value:
        out["credentialArn"] = value["credential_arn"]
    if "custom_role_arn" in value:
        out["customRoleArn"] = value["custom_role_arn"]
    if "upstream_repository_prefix" in value:
        out["upstreamRepositoryPrefix"] = value["upstream_repository_prefix"]
    if "upstream_registry" in value:
        import aws_sdk_ecr.types.upstream_registry

        out["upstreamRegistry"] = (
            aws_sdk_ecr.types.upstream_registry.serialize_aws_json_1_1(
                value["upstream_registry"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_ecr.types.updated_timestamp

        out["updatedAt"] = aws_sdk_ecr.types.updated_timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PullThroughCacheRule:
    out: PullThroughCacheRule = {}  # type: ignore[typeddict-item]
    if "ecrRepositoryPrefix" in data:
        out["ecr_repository_prefix"] = data["ecrRepositoryPrefix"]
    if "upstreamRegistryUrl" in data:
        out["upstream_registry_url"] = data["upstreamRegistryUrl"]
    if "createdAt" in data:
        import aws_sdk_ecr.types.creation_timestamp

        out["created_at"] = (
            aws_sdk_ecr.types.creation_timestamp.deserialize_aws_json_1_1(
                data["createdAt"]
            )
        )
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "credentialArn" in data:
        out["credential_arn"] = data["credentialArn"]
    if "customRoleArn" in data:
        out["custom_role_arn"] = data["customRoleArn"]
    if "upstreamRepositoryPrefix" in data:
        out["upstream_repository_prefix"] = data["upstreamRepositoryPrefix"]
    if "upstreamRegistry" in data:
        import aws_sdk_ecr.types.upstream_registry

        out["upstream_registry"] = (
            aws_sdk_ecr.types.upstream_registry.deserialize_aws_json_1_1(
                data["upstreamRegistry"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_ecr.types.updated_timestamp

        out["updated_at"] = (
            aws_sdk_ecr.types.updated_timestamp.deserialize_aws_json_1_1(
                data["updatedAt"]
            )
        )
    return out
