"""Generated from Smithy shape ``com.amazonaws.ecr#ValidatePullThroughCacheRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.credential_arn
    import aws_sdk_ecr.types.custom_role_arn
    import aws_sdk_ecr.types.is_ptc_rule_valid
    import aws_sdk_ecr.types.ptc_validate_failure
    import aws_sdk_ecr.types.pull_through_cache_rule_repository_prefix
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.url


class ValidatePullThroughCacheRuleResponse(TypedDict):
    ecr_repository_prefix: NotRequired[
        "aws_sdk_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix"
    ]
    """<p>The Amazon ECR repository prefix associated with the pull through cache rule.</p>"""
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    upstream_registry_url: NotRequired["aws_sdk_ecr.types.url.Url"]
    """<p>The upstream registry URL associated with the pull through cache rule.</p>"""
    credential_arn: NotRequired["aws_sdk_ecr.types.credential_arn.CredentialArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret associated with the pull through cache rule.</p>"""
    custom_role_arn: NotRequired["aws_sdk_ecr.types.custom_role_arn.CustomRoleArn"]
    """<p>The ARN of the IAM role associated with the pull through cache rule.</p>"""
    upstream_repository_prefix: NotRequired[
        "aws_sdk_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix"
    ]
    """<p>The upstream repository prefix associated with the pull through cache rule.</p>"""
    is_valid: "aws_sdk_ecr.types.is_ptc_rule_valid.IsPTCRuleValid"
    """<p>Whether or not the pull through cache rule was validated. If <code>true</code>, Amazon ECR was able to reach the upstream registry and authentication was successful. If <code>false</code>, there was an issue and validation failed. The <code>failure</code> reason indicates the cause.</p>"""
    failure: NotRequired["aws_sdk_ecr.types.ptc_validate_failure.PTCValidateFailure"]
    """<p>The reason the validation failed. For more details about possible causes and how to address them, see <a href=\"https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache.html\">Using pull through cache rules</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidatePullThroughCacheRuleResponse) -> dict:
    out: dict = {}
    if "ecr_repository_prefix" in value:
        out["ecrRepositoryPrefix"] = value["ecr_repository_prefix"]
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "upstream_registry_url" in value:
        out["upstreamRegistryUrl"] = value["upstream_registry_url"]
    if "credential_arn" in value:
        out["credentialArn"] = value["credential_arn"]
    if "custom_role_arn" in value:
        out["customRoleArn"] = value["custom_role_arn"]
    if "upstream_repository_prefix" in value:
        out["upstreamRepositoryPrefix"] = value["upstream_repository_prefix"]
    out["isValid"] = value.get("is_valid", False)
    if "failure" in value:
        out["failure"] = value["failure"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidatePullThroughCacheRuleResponse:
    out: ValidatePullThroughCacheRuleResponse = {}  # type: ignore[typeddict-item]
    if "ecrRepositoryPrefix" in data:
        out["ecr_repository_prefix"] = data["ecrRepositoryPrefix"]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "upstreamRegistryUrl" in data:
        out["upstream_registry_url"] = data["upstreamRegistryUrl"]
    if "credentialArn" in data:
        out["credential_arn"] = data["credentialArn"]
    if "customRoleArn" in data:
        out["custom_role_arn"] = data["customRoleArn"]
    if "upstreamRepositoryPrefix" in data:
        out["upstream_repository_prefix"] = data["upstreamRepositoryPrefix"]
    if "isValid" in data:
        out["is_valid"] = data["isValid"]
    else:
        out["is_valid"] = False
    if "failure" in data:
        out["failure"] = data["failure"]
    return out
