"""Generated from Smithy shape ``com.amazonaws.omics#RegistryMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.aws_account_id
    import aws_sdk_omics.types.ecr_repository_prefix
    import aws_sdk_omics.types.upstream_repository_prefix
    import aws_sdk_omics.types.uri


class RegistryMapping(TypedDict):
    upstream_registry_url: NotRequired["aws_sdk_omics.types.uri.Uri"]
    """<p>The URI of the upstream registry.</p>"""
    ecr_repository_prefix: NotRequired[
        "aws_sdk_omics.types.ecr_repository_prefix.EcrRepositoryPrefix"
    ]
    """<p>The repository prefix to use in the ECR private repository.</p>"""
    upstream_repository_prefix: NotRequired[
        "aws_sdk_omics.types.upstream_repository_prefix.UpstreamRepositoryPrefix"
    ]
    """<p>The repository prefix of the corresponding repository in the upstream registry.</p>"""
    ecr_account_id: NotRequired["aws_sdk_omics.types.aws_account_id.AwsAccountId"]
    """<p>Account ID of the account that owns the upstream container image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistryMapping) -> dict:
    out: dict = {}
    if "upstream_registry_url" in value:
        out["upstreamRegistryUrl"] = value["upstream_registry_url"]
    if "ecr_repository_prefix" in value:
        out["ecrRepositoryPrefix"] = value["ecr_repository_prefix"]
    if "upstream_repository_prefix" in value:
        out["upstreamRepositoryPrefix"] = value["upstream_repository_prefix"]
    if "ecr_account_id" in value:
        out["ecrAccountId"] = value["ecr_account_id"]
    return out


def deserialize_json(data: dict) -> RegistryMapping:
    out: RegistryMapping = {}  # type: ignore[typeddict-item]
    if "upstreamRegistryUrl" in data:
        out["upstream_registry_url"] = data["upstreamRegistryUrl"]
    if "ecrRepositoryPrefix" in data:
        out["ecr_repository_prefix"] = data["ecrRepositoryPrefix"]
    if "upstreamRepositoryPrefix" in data:
        out["upstream_repository_prefix"] = data["upstreamRepositoryPrefix"]
    if "ecrAccountId" in data:
        out["ecr_account_id"] = data["ecrAccountId"]
    return out
